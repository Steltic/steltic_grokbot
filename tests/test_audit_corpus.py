"""The corpus audit must see what a query cannot: another document's text under this one's ids,
a document indexed twice, commentary tagged as provisions, LaTeX printed with another equation's
id, a table of contents posing as a numbered table.

Engine-free and corpus-free: run with `python -m pytest tests -q` from the repo root.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from audit_corpus import audit, render_md  # noqa: E402


def _workspace(tmp_path, sections, equations=(), tables=(), boundary=211, pages=358):
    idx = tmp_path / "indexes"
    idx.mkdir()
    (idx / "documents.json").write_text(json.dumps([{
        "id": "AISC_358_22", "converted_stem": "A358_22", "collection": "specification",
        "title": "ANSI/AISC 358-22 Prequalified Connections", "pdf_pages_total": pages,
        "commentary_boundary": {"cover_pdf_page": boundary},
    }]), encoding="utf-8")
    (idx / "sections.json").write_text(json.dumps(list(sections)), encoding="utf-8")
    (idx / "equations.json").write_text(json.dumps(list(equations)), encoding="utf-8")
    (idx / "tables.json").write_text(json.dumps(list(tables)), encoding="utf-8")
    (idx / "build_stats.json").write_text(json.dumps({"id_collisions": []}), encoding="utf-8")
    return tmp_path


def _sec(sid, page, part="standard", chunk="A358_22_p046_050.json", title="Title"):
    return {"doc": "AISC_358_22", "section_id": sid, "title": title, "pdf_page": page, "part": part, "chunk": chunk}


def _codes(report, level=None):
    return {f["code"] for f in report["findings"] if level is None or f["level"] == level}


def test_a_clean_index_has_no_fail(tmp_path):
    ws = _workspace(tmp_path, [_sec("5.1", 45), _sec("5.7", 49), _sec("5.7", 234, "commentary")] * 1)
    rep = audit(ws, smoke=False)
    assert rep["counts"]["FAIL"] == 0, rep["findings"]


def test_another_documents_chunk_is_a_fail(tmp_path):
    ws = _workspace(tmp_path, [_sec("5.1", 45), _sec("J1", 195, chunk="A341_22_p191_195.json", title="GENERAL PROVISIONS")])
    rep = audit(ws, smoke=False)
    assert "foreign-chunk" in _codes(rep, "FAIL")


def test_an_appended_duplicate_layer_is_a_fail(tmp_path):
    ws = _workspace(tmp_path, [_sec("5.1", 45), _sec("5.1", 45)])
    assert "duplicate-sections" in _codes(audit(ws, smoke=False), "FAIL")


def test_commentary_served_as_standard_is_a_fail(tmp_path):
    ws = _workspace(tmp_path, [_sec("5.1", 45), _sec("5.7", 234, "standard")])   # pdf 234 is past the cover (211)
    assert "commentary-as-standard" in _codes(audit(ws, smoke=False), "FAIL")


def test_latex_printed_with_another_id_is_a_fail(tmp_path):
    eq = [{"doc": "AISC_358_22", "eq_id": "5.7-2", "part": "standard", "latex": "M_{pr} = C_{pr} R_y F_y Z_e & & ( 5 . 7 - 1 )"}]
    ws = _workspace(tmp_path, [_sec("5.1", 45)], equations=eq)
    assert "latex-wrong-equation" in _codes(audit(ws, smoke=False), "FAIL")


def test_a_table_of_contents_with_an_id_is_a_fail(tmp_path):
    tb = [{"doc": "AISC_358_22", "table_id": "6.1", "printed_label": "9.2-xviii", "pdf_page": 20, "part": "standard"}]
    ws = _workspace(tmp_path, [_sec("5.1", 45)], tables=tb)
    assert "front-matter-table-id" in _codes(audit(ws, smoke=False), "FAIL")


def test_the_report_names_the_document_and_the_fault(tmp_path):
    ws = _workspace(tmp_path, [_sec("5.1", 45), _sec("J1", 195, chunk="A341_22_p191_195.json")])
    md = render_md(audit(ws, smoke=False))
    assert "FAIL" in md and "AISC_358_22" in md and "foreign-chunk" in md
