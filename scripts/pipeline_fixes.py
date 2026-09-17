"""Rebuild-enforced conversion/retrieval rules. Imported by retrieval, postprocess, build_index."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

WS_RE = re.compile(r"\s+")


def collapse_ws(text: str) -> str:
    return WS_RE.sub(" ", text or "").strip()


def section_depth(sid: Optional[str]) -> int:
    if not sid:
        return 0
    return sid.count(".") + sid.count("-") + len(re.findall(r"[a-z]$", sid))


def is_descendant(child: Optional[str], parent: Optional[str]) -> bool:
    if not child or not parent or child == parent:
        return False
    if child.startswith(parent + "."):
        return True
    rest = child[len(parent) :] if child.startswith(parent) else ""
    return bool(rest) and re.fullmatch(r"[A-Za-z]", rest) is not None


def heading_positions(text: str, sid: str) -> list[int]:
    """All heading offsets for sid. Includes AISC implied '## 4a.' for E3.4a."""
    if not sid or not text:
        return []
    esc = re.escape(sid)
    # (?!\.\d) so E1.4.1 does not match child E1.4.1.4 (\b is true before '.')
    bnd = r"(?![.\d])"
    patterns = [
        rf"(?m)^#{{1,6}}\s*{esc}(?!\.\d)",
        rf"(?m)^#{{1,6}}\s*{esc}\.(?:\s|$)",
        rf"(?m)^{esc}\.(?:\s|$)",
        rf"(?m)^{esc}\s+[A-Z(]",
        rf"(?m)^#{{1,6}}\s+{esc}\s",
    ]
    m_let = re.match(r"^(.+\d)([a-z])$", sid)
    if m_let:
        last = re.search(r"(\d+[a-z])$", sid)
        if last:
            patterns.append(rf"(?m)^#{{1,6}}\s*{last.group(1)}\.\s")
        patterns.append(rf"(?m)^#{{1,6}}\s*{m_let.group(2)}\.\s")
    hits: list[int] = []
    for pat in patterns:
        for m in re.finditer(pat, text):
            hits.append(m.start())
    if not hits:
        for m in re.finditer(rf"(?m)^(?:#{{1,6}}\s*)?{esc}\b", text):
            hits.append(m.start())
    return sorted(dict.fromkeys(hits))


def find_heading_pos(text: str, sid: str, *, which: str = "first") -> Optional[int]:
    hits = heading_positions(text, sid)
    if not hits:
        return None
    return hits[-1] if which == "last" else hits[0]


def is_toc_nomenclature_table(rec: dict[str, Any]) -> bool:
    title = rec.get("title") or ""
    ex = rec.get("markdown_excerpt") or ""
    if re.search(r"for the corresponding", title, re.I):
        return True
    if re.search(r"\.\s+\.\s+\.", title):
        return True
    if re.search(r"Symbol\s*\|\s*Definition", ex):
        return True
    return False


def orig_is_phi_omega_only(orig: str) -> bool:
    o = collapse_ws(orig or "")
    if not o:
        return False
    if re.search(r"\b[RMPVH]n\b", o, re.I) or re.search(r"[MNPV]_\s*n", o):
        return False
    has_phi = bool(re.search(r"[φϕΦ]|phi\b", o, re.I))
    has_omega = bool(re.search(r"[ΩΩω]|omega\b", o, re.I))
    has_lrfd = bool(re.search(r"LRFD|ASD", o, re.I))
    return (has_phi or has_omega) and has_lrfd and "=" in o and len(o) < 90


def orig_cites_other_eq(orig: str, eq_id: str) -> bool:
    if not orig or not eq_id:
        return False
    ids = re.findall(r"\(([A-Z]?\d[\w.\-]*\d[A-Za-z]?)\)", orig)
    ids += re.findall(r"\bEq\.?\s*([A-Z]?\d[\w.\-]*\d[A-Za-z]?)", orig, re.I)
    for i in ids:
        if i != eq_id and not eq_id.endswith(i):
            return True
    return False


def example_id_matches(query: str, cid: str) -> bool:
    q = (query or "").strip()
    c = (cid or "").strip()
    if not q or not c:
        return False
    if c == q or c == q + "_p1":
        return True
    if c.startswith(q):
        rest = c[len(q) :]
        if rest.startswith(("_p", "-", "_")):
            return True
    return False


def looks_like_example_id(query: str) -> bool:
    q = (query or "").strip()
    return bool(re.match(r"^[A-Z]\.\d", q))


def table_id_from_title(title: str) -> Optional[str]:
    if not title:
        return None
    m = re.search(
        r"\bTABLE\s+((?:C-)?(?:[A-Z]-)?(?:[A-Z]?\d+(?:\.\d+)*[A-Za-z]?)(?:-\d+[A-Za-z]?)?)\b",
        title,
        re.I,
    )
    if not m:
        return None
    return re.sub(r"\s+", "", m.group(1))


def inherit_continued_table_ids(tables: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Assign table_id on adjacent continued pages (ASCE 12.2-1 gold: 173-175).

    A null-id grid on page N inherits the previous page's real table_id when
    |N - prev| == 1. Title 'TABLE X (Continued)' also inherits X.
    """
    by_doc: dict[str, list[dict[str, Any]]] = {}
    for t in tables:
        by_doc.setdefault(str(t.get("doc") or ""), []).append(t)
    for _doc, rows in by_doc.items():
        rows.sort(key=lambda r: (int(r.get("pdf_page") or 0), str(r.get("table_id") or "")))
        last_tid = None
        last_page = None
        last_part = None
        for t in rows:
            p = int(t.get("pdf_page") or 0)
            part = t.get("part")
            tid = t.get("table_id")
            title = t.get("title") or ""
            from_title = table_id_from_title(title)
            caption_like = bool(
                re.search(
                    r"Safety Factors|Design Coef|Listed Materials|Continued|Resistance Factors",
                    title,
                    re.I,
                )
                or len(title) > 28
            )
            if from_title and caption_like and (
                not tid
                or (
                    tid
                    and from_title.lower().startswith(str(tid).lower())
                    and from_title.lower() != str(tid).lower()
                )
            ):
                t["table_id"] = from_title
                tid = from_title
            if not tid:
                cont = bool(re.search(r"continued", title, re.I))
                if last_tid and last_page and part == last_part and p - last_page == 1:
                    t["table_id"] = last_tid
                    tid = last_tid
                    issues = list(t.get("issues") or [])
                    msg = "continued table_id inherited from adjacent page"
                    if msg not in issues:
                        issues.append(msg)
                    t["issues"] = issues
                elif cont and last_tid:
                    t["table_id"] = last_tid
                    tid = last_tid
            if tid:
                last_tid = tid
                last_page = p
                last_part = part
            elif last_page is not None and p - last_page > 1:
                last_tid = None
                last_part = None
    return tables


def adjacent_null_table_pages(tables: list[dict[str, Any]], rec: dict[str, Any]) -> list[dict[str, Any]]:
    """Null-id tables on pages between first and last page of this table_id."""
    doc = rec.get("doc")
    tid = rec.get("table_id")
    part = rec.get("part")
    if not doc or not tid:
        return []
    same = [
        t
        for t in tables
        if t.get("doc") == doc and t.get("table_id") == tid and t.get("part") == part and t.get("pdf_page")
    ]
    if not same:
        return []
    pages = [int(t["pdf_page"]) for t in same]
    lo, hi = min(pages), max(pages)
    extras = []
    for t in tables:
        if t.get("doc") != doc or not t.get("pdf_page"):
            continue
        p = int(t["pdf_page"])
        if lo <= p <= hi and not t.get("table_id"):
            extras.append(t)
    return extras


def example_family_ids(sections: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    q = (query or "").strip()
    out = []
    for s in sections:
        if s.get("collection") == "specification":
            continue
        cid = s.get("id") or ""
        if example_id_matches(q, cid):
            out.append(s)
    out.sort(key=lambda s: s.get("id") or "")
    return out


def build_example_id_aliases(sections: list[dict[str, Any]]) -> dict[str, list[str]]:
    aliases: dict[str, list[str]] = {}
    for s in sections:
        if s.get("collection") == "specification":
            continue
        cid = s.get("id") or ""
        m = re.match(r"^(.+)_p\d+$", cid)
        if not m:
            continue
        base = m.group(1)
        aliases.setdefault(base, []).append(cid)
        m2 = re.match(r"^([A-Z]\.\d+)(?=-|_|$)", base)
        if m2 and m2.group(1) != base:
            aliases.setdefault(m2.group(1), []).append(cid)
    for k, vs in aliases.items():
        aliases[k] = list(dict.fromkeys(vs))
    return aliases


def pdf_page_text(pdf_path: Path, page: int) -> str:
    """One page of a PDF as text: pdftotext -layout when Poppler is on PATH, else pypdfium2.

    The third and last call site that shelled out to `pdftotext` unconditionally -- on a Windows
    machine without Poppler that raises FileNotFoundError before any check, here in the middle of
    the equation repair pass. See pdftext.py."""
    if not pdf_path or not Path(pdf_path).is_file() or not page:
        return ""
    try:
        from pdftext import pdf_page_text as _page
    except ImportError:                        # imported as a loose module, not from scripts/
        import sys
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from pdftext import pdf_page_text as _page
    return _page(pdf_path, int(page))
