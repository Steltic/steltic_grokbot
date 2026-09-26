"""A table answered without its footnotes is a table the reader cannot use.

AISC 342-22 Table C5.5 gives the FR-connection rows' `a` as "X1 <= 0.07" / "X2 <= 0.07" and defines X1
and X2 in footnotes [d] and [e]: equations with no number, so `exact_equation` cannot reach them and
keyword search skips equation records without an id. On the converted page the X2 line is truncated at
"(L/d)^{0."; the equation index has it whole. And a continued page used to contribute only its excerpt
(the head of the table), so the RBS row -- last on the continued page -- was not in the answer at all.
These tests build a small corpus in the file layout retrieval.py reads and pin both.
"""
import json
import os
import sys

from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from retrieval import Corpus  # noqa: E402

RBS = "| RBS moment connection in conformance with ANSI/AISC 358 [b][e] | X 2 0 07 ≤ . | 0.07 | 0.3 | 0.5 a | 0.75 b | b |"
X2 = ("[ \\mathbf e ] _ { X _ { 2 } = 0 . 5 5 } ( \\frac { h } { t _ { w } } ) ^ { - 0 . 5 } \\left ( \\frac { b _ { f } } { 2 t _ { f } } "
      "\\right ) ^ { - 0 . 7 } \\left ( \\frac { L _ { b } } { r _ { y } } \\right ) ^ { - 0 . 5 } \\left ( \\frac { L } { d } \\right ) ^ { 0 . 8 }")


def _corpus(tmp_path: Path) -> Corpus:
    # the layout find_root() recognises: documents/standards + scripts, indexes at the root
    (tmp_path / "documents" / "standards").mkdir(parents=True); (tmp_path / "scripts").mkdir()
    idx = tmp_path / "indexes"; idx.mkdir(parents=True)
    pages = tmp_path / "markdown" / "pages"; pages.mkdir(parents=True)
    (idx / "documents.json").write_text(json.dumps([{"doc": "AISC_342_22", "title": "AISC 342-22", "stem": "AISC_342_22", "collection": "specification"}]), encoding="utf-8")
    (idx / "sections.json").write_text("[]", encoding="utf-8")
    (idx / "tables.json").write_text(json.dumps([
        {"doc": "AISC_342_22", "table_id": "C5.5", "title": "", "front_matter": False, "section": "C5.4a", "part": "standard",
         "pdf_pages": [109], "pdf_page": 109, "printed_label": "77", "num_rows": 11, "num_cols": 7, "collection": "specification",
         "markdown_excerpt": "## TABLE C5.5\n| WUF (pre-1995) [b] | 0 048 0 0011 . . - d b |"},
        {"doc": "AISC_342_22", "table_id": "C5.5", "title": "", "front_matter": False, "section": "C5.4b", "part": "standard",
         "pdf_pages": [110], "pdf_page": 110, "printed_label": "78", "num_rows": 8, "num_cols": 7, "collection": "specification",
         "markdown_excerpt": "## TABLE C5.5 (continued)\n| Welded flange plates | | |"},
    ]), encoding="utf-8")
    (idx / "equations.json").write_text(json.dumps([
        {"doc": "AISC_342_22", "eq_id": None, "section": "C5.4b", "part": "standard", "pdf_page": 110, "printed_label": "78",
         "latex": X2, "orig": "[e] X ...", "nearby_text": "", "issues": [], "collection": "specification"},
        {"doc": "AISC_342_22", "eq_id": None, "section": "C5.4b", "part": "standard", "pdf_page": 110, "printed_label": "78",
         "latex": "& 0 . 3 \\left ( \\frac { - } { t _ { w } } \\right )", "orig": "", "nearby_text": "", "issues": [], "collection": "specification"},
        {"doc": "AISC_342_22", "eq_id": "C5-21", "section": "C5.4a", "part": "standard", "pdf_page": 108, "printed_label": "76",
         "latex": "V _ { pz } = ...", "orig": "", "nearby_text": "", "issues": [], "collection": "specification"},
    ]), encoding="utf-8")
    for pg, body in ((109, "## TABLE C5.5\n\n| WUF (pre-1995) [b] | 0 048 0 0011 . . - d b |\n"),
                     (110, "## TABLE C5.5 (continued)\n\n| Welded flange plates | | |\n" + RBS + "\n\n$$" + X2[:180] + "$$\n")):
        (pages / ("A342_22_p%03d.md" % pg)).write_text(body, encoding="utf-8")
    c = Corpus(tmp_path)
    assert c.root == tmp_path, c.root
    # the page bodies, without depending on how this build of retrieval.py finds page files
    c._pages = {"AISC_342_22": {109: {"body": (pages / "A342_22_p109.md").read_text(encoding="utf-8")},
                            110: {"body": (pages / "A342_22_p110.md").read_text(encoding="utf-8")}}}
    return c


def test_exact_table_returns_the_continued_pages_rows(tmp_path):
    c = _corpus(tmp_path)
    r = c.exact_table("C5.5", doc="AISC_342_22")
    assert r["found"] and len(r["hits"]) == 1
    assert "RBS moment connection in conformance" in r["hits"][0]["text"]


def test_exact_table_carries_its_footnote_equations_whole(tmp_path):
    c = _corpus(tmp_path)
    h = c.exact_table("C5.5", doc="AISC_342_22")["hits"][0]
    assert "FOOTNOTE EQUATIONS" in h["text"]
    assert "0 . 8 }" in h["text"], "the L/d exponent the page text lost"
    assert [e["pdf_page"] for e in h["footnote_equations"]] == [110]
    assert not any(e["latex"].startswith("&") for e in h["footnote_equations"]), "alignment fragments are not footnotes"
    # a numbered equation on another page of the section is not a footnote of this table
    assert "C5-21" not in h["text"]
