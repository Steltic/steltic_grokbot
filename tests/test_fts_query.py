"""The FTS5 query builder: the two faults that made a populated corpus look empty.

Both were live on 2026-09-18, and both are invisible from the outside -- the corpus was correct,
the index was correct, and every query came back with a plausible-looking answer:

  1. `E3.4a` reached FTS5 with its dot intact, FTS5 raised `syntax error near "."`, and the caller
     swallowed it with a bare `except sqlite3.OperationalError: continue`. Exact printed clause ids
     -- the form the design contract tells the agent to use -- contributed nothing at all.
  2. `lateral-torsional` was split into two loose terms. FTS5 ANDs space-separated terms, so
     "flexural strength compact I-shape lateral-torsional buckling F2" went out as a nine-term AND
     and matched one chunk in the whole of AISC 360-22.

Engine-free and corpus-free: run with `python -m pytest tests -q` from the repo root.
"""
import os
import re
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from retrieval import fts_escape, fts_strategies  # noqa: E402

A360 = "flexural strength compact I-shape lateral-torsional buckling F2"
A341 = "special moment frame strong column weak beam SCWB ratio E3.4a"


def _fts():
    """A tiny in-memory index with the same column layout as spec_fts."""
    con = sqlite3.connect(":memory:")
    con.execute("CREATE VIRTUAL TABLE spec_fts USING fts5(section_id, title, body)")
    rows = [
        ("F2", "DOUBLY SYMMETRIC COMPACT I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MAJOR AXIS",
         "This section applies to doubly symmetric I-shaped members and channels."),
        ("F2.1", "Yielding", "The nominal flexural strength Mn shall be the lower value obtained."),
        ("F2.2", "Lateral-Torsional Buckling",
         "When Lb exceeds Lp the limit state of lateral-torsional buckling applies."),
        ("E3.4a", "Moment Ratio",
         "The strong-column weak-beam moment ratio shall satisfy the following relationship."),
        ("G2.1", "Shear Strength", "The nominal shear strength of webs without tension field action."),
    ]
    con.executemany("INSERT INTO spec_fts VALUES (?,?,?)", rows)
    return con


def _run(con, expr):
    return [r[0] for r in con.execute(
        "SELECT section_id FROM spec_fts WHERE spec_fts MATCH ? ORDER BY bm25(spec_fts)", (expr,))]


# --- fault 1: the dot ---------------------------------------------------------------------------

def test_a_dotted_clause_id_is_legal_fts():
    con = _fts()
    for q in ("E3.4a", "F2.2", "16.1.2", "C-F2.1", "D1.1a"):
        expr = fts_escape(q)
        con.execute("SELECT count(*) FROM spec_fts WHERE spec_fts MATCH ?", (expr,))   # must not raise


def test_every_strategy_is_parseable():
    con = _fts()
    for q in (A360, A341, "panel zone E3.6e", "G2.2 tension field action", "drift"):
        for label, expr in fts_strategies(q):
            con.execute("SELECT count(*) FROM spec_fts WHERE spec_fts MATCH ?", (expr,)), label


def test_an_exact_id_finds_its_own_clause():
    con = _fts()
    assert "E3.4a" in _run(con, fts_escape("E3.4a"))


# --- fault 2: the hyphen and the nine-term AND ---------------------------------------------------

def test_a_hyphenated_compound_stays_one_phrase():
    # not `lateral torsional` as two independent terms, which is what grew the AND
    assert '"lateral torsional"' in fts_escape("lateral-torsional buckling")


def test_strict_first_then_progressively_looser():
    labels = [lbl for lbl, _ in fts_strategies(A360)]
    assert labels[0] == "strict"
    assert "id-anchored" in labels
    assert labels == sorted(set(labels), key=labels.index)      # no repeats


def test_the_id_stays_mandatory_when_the_prose_is_loosened():
    expr = dict((l, e) for l, e in fts_strategies(A360))["id-anchored"]
    assert expr.startswith("F2 AND (") and " OR " in expr


def test_the_real_query_reaches_f2_2_after_loosening():
    con = _fts()
    assert _run(con, fts_escape(A360)) == []                    # the nine-term AND, as it was
    hits = []
    for _, expr in fts_strategies(A360):
        hits = _run(con, expr)
        if len(hits) >= 3:
            break
    assert "F2.2" in hits and "F2" in hits and "F2.1" in hits


def test_function_words_are_dropped_but_engineering_words_are_not():
    expr = fts_escape("the nominal flexural strength of a compact section")
    assert "the" not in expr.split() and "of" not in expr.split()
    for keep in ("nominal", "flexural", "strength", "compact", "section"):
        assert keep in expr.split()


def test_a_handwritten_fts_expression_is_left_alone():
    q = 'F2 AND (flexural OR buckling)'
    assert fts_escape(q) == q
    assert fts_strategies(q) == [("verbatim", q)]


# --- the ids a question names, and what they are for ---------------------------------------------

def test_the_ids_a_question_names_are_recognised():
    from retrieval import fts_ids
    assert fts_ids(A360) == ["F2"]
    assert fts_ids(A341) == ["E3.4A"]
    assert fts_ids("panel zone shear strength E3.6e") == ["E3.6E"]
    assert fts_ids("tension field action G2.2 and equation G2-6") == ["G2.2", "G2-6"]


def test_prose_is_not_mistaken_for_an_id():
    from retrieval import fts_ids
    for q in ("lateral-torsional buckling of compact shapes",
              "strong column weak beam",
              "acceptance criteria for nonlinear procedures"):
        assert fts_ids(q) == [], q


def test_an_id_without_digits_is_not_an_id():
    from retrieval import fts_ids
    # 'RBS', 'SCBF', 'WUF-W' are abbreviations, not clause numbers
    assert fts_ids("RBS SCBF WUF-W BFP connections") == []
