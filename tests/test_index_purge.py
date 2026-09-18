"""Re-processing a document must replace its records, not pile a fresh set beside the stale one.

The fault this guards against was live on 2026-09-18. postprocess.py writes a document's records
under its filename stem ("A358_22"); build_index.py reads the same flat `indexes/` set, re-keys
every record under the canonical id ("AISC_358_22") and writes its output back over the same
files. postprocess's purge compared against the stem alone, so after any build it purged nothing
and every re-process appended: AISC 358-22 carried 2612 section records of which 1905 named an
AISC 341/360 chunk file, and every re-processed document held a full duplicate layer. Four rounds
of retrieval fixes were correct and moved nothing, because the records being queried were wrong.

A second fault sat beside it: convert_pdf.py writes to `indexes/converted/` while the hub's
Re-process tab writes to `indexes/`, and build_index read only whichever existed first -- the next
PDF converted would have made the rebuild index one document and drop the other five.

Engine-free and corpus-free: run with `python -m pytest tests -q` from the repo root.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from postprocess import document_names, purge_document  # noqa: E402
from build_index import discover_specs  # noqa: E402


def _rec(doc, sid, **kw):
    return {"doc": doc, "section_id": sid, **kw}


# --- the purge -------------------------------------------------------------------------------

def test_a_document_answers_to_every_name_it_is_filed_under():
    names = document_names("A358_22")
    assert {"A358_22", "AISC_358_22"} <= names
    assert "AISC_341_22" not in names
    assert {"asce41_23", "ASCE_41_23"} <= document_names("asce41_23")


def test_purge_drops_stem_canonical_and_converted_stem_records_only():
    existing = [
        _rec("A358_22", "5.1"),                                   # the converter's own, last run
        _rec("AISC_358_22", "J1", chunk="A341_22_p191_195.json"), # the builder's re-keyed copy
        {"id": "AISC_358_22", "converted_stem": "A358_22"},       # the builder's document record
        _rec("AISC_341_22", "F2"),                                # another document: untouched
        _rec("opensees", "x"),                                    # phase-2: untouched
    ]
    kept = purge_document(existing, "A358_22", "doc", "A358_22")
    assert [r.get("doc") or r.get("id") for r in kept] == ["AISC_341_22", "opensees"]


def test_reprocessing_twice_leaves_the_record_count_unchanged():
    """The merge postprocess performs is purge-then-append; run it twice and nothing accumulates."""
    fresh = [_rec("A358_22", s) for s in ("1.1", "1.2", "5.1", "5.8")]
    stale = [_rec("AISC_358_22", "J1", chunk="A341_22_p191_195.json"), _rec("AISC_358_22", "5.1")]
    other = [_rec("AISC_360_22", "E3")]
    store = other + stale
    once = purge_document(store, "A358_22") + fresh
    twice = purge_document(once, "A358_22") + fresh
    assert len(once) == len(other) + len(fresh)
    assert len(twice) == len(once)
    assert not [r for r in twice if r.get("chunk", "A358_22_").startswith("A341_22_")]


# --- discovery across both index locations -------------------------------------------------

def _write(d, docs, secs):
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "documents.json"), "w", encoding="utf-8") as f:
        json.dump(docs, f)
    with open(os.path.join(d, "sections.json"), "w", encoding="utf-8") as f:
        json.dump(secs, f)


def test_legacy_and_converted_index_sets_are_both_read(tmp_path):
    root = tmp_path
    # the legacy set: a previous build's output for two documents (canonical ids, stamped)
    _write(root / "indexes", [
        {"id": "AISC_360_22", "converted_stem": "A360_22", "collection": "specification"},
        {"id": "AISC_341_22", "converted_stem": "A341_22", "collection": "specification"},
    ], [_rec("AISC_360_22", "E3"), _rec("AISC_341_22", "F2")])
    # converted/: a fresh conversion of one of them (the converter writes stems, no `collection`)
    _write(root / "indexes" / "converted", [{"id": "A360_22"}], [_rec("A360_22", "E3"), _rec("A360_22", "E4")])

    specs = discover_specs(root)
    by_canon = {s["canonical"]: s for s in specs}
    assert set(by_canon) == {"AISC_360_22", "AISC_341_22"}, "one location must not hide the other"
    assert by_canon["AISC_360_22"]["stem"] == "A360_22", "the conversion wins over the build's copy"
    assert len(by_canon["AISC_360_22"]["sections"]) == 2
    assert len(by_canon["AISC_341_22"]["sections"]) == 1
    assert len(specs) == 2, "a document described in both places is indexed once"


def test_the_converted_folder_wins_over_a_legacy_converter_record(tmp_path):
    """A converter record left in the legacy set (an old hub Re-process tab) must not shadow the
    set the converter writes to now, or a rebuild would flip between the two."""
    root = tmp_path
    _write(root / "indexes" / "converted", [{"id": "A358_22"}], [_rec("A358_22", "kept")])
    _write(root / "indexes", [{"id": "A358_22"}], [_rec("A358_22", "legacy"), _rec("A358_22", "legacy2")])
    specs = discover_specs(root)
    assert len(specs) == 1
    assert [r["section_id"] for r in specs[0]["sections"]] == ["kept"]


def test_the_converter_never_writes_into_the_builders_output_folder(tmp_path):
    from postprocess import converter_indexes_dir
    root = tmp_path
    assert converter_indexes_dir(root, root / "indexes") == root / "indexes" / "converted"
    assert converter_indexes_dir(root, root / "indexes" / "converted") == root / "indexes" / "converted"
    assert converter_indexes_dir(root, root / "elsewhere") == root / "elsewhere"
