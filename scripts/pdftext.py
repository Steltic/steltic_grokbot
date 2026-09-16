"""Page text from a PDF, whichever extractor this machine has.

Poppler's ``pdftotext -layout`` is the first choice: its column-aware layout is what the table
recovery and the equation census were written against. It is rarely on a Windows PATH, though, and
``subprocess.run(["pdftotext", ...])`` there raises FileNotFoundError before any of our warnings --
which is how a successful conversion used to end in a traceback from postprocess.py.

The fallback is pypdfium2, which Docling installs (convert_pdf.py already uses it for the page
count): reading-order text per page, no layout columns, good enough for searchable tokens and for
finding "(E3-1)"-style ids. Which one was used is logged once, and ``describe()`` says so for the
conversion metadata.
"""
from __future__ import annotations

import logging
import shutil
import subprocess
from pathlib import Path
from typing import Optional

LOG = logging.getLogger("pdftext")
_ANNOUNCED: set[str] = set()


def have_pdftotext() -> bool:
    return shutil.which("pdftotext") is not None


def describe() -> str:
    """Which extractor a call would use right now."""
    if have_pdftotext():
        return "pdftotext"
    try:
        import pypdfium2  # noqa: F401
        return "pypdfium2"
    except ImportError:
        return "none"


def _announce(which: str, why: str = "") -> None:
    if which in _ANNOUNCED:
        return
    _ANNOUNCED.add(which)
    if which == "pdftotext":
        LOG.info("page text via pdftotext -layout (Poppler)")
    elif which == "pypdfium2":
        LOG.warning("pdftotext (Poppler) not on PATH%s -- page text via pypdfium2 (reading order, no layout columns); "
                    "install Poppler and put pdftotext on PATH for column-aware table recovery", why)
    else:
        LOG.warning("no page-text extractor: pdftotext (Poppler) is not on PATH and pypdfium2 is not installed -- "
                    "equation census and image-page recovery skipped")


def _via_pdftotext(pdf_path: Path, first: Optional[int], last: Optional[int]) -> Optional[list[str]]:
    cmd = ["pdftotext", "-layout"]
    if first:
        cmd += ["-f", str(first)]
    if last:
        cmd += ["-l", str(last)]
    cmd += [str(pdf_path), "-"]
    try:
        r = subprocess.run(cmd, capture_output=True, check=False, encoding="utf-8", errors="replace")
    except OSError as e:                      # present in which() but not runnable, or gone since
        _announce("pypdfium2", f" ({e.__class__.__name__})")
        return None
    if r.returncode != 0:
        LOG.warning("pdftotext failed rc=%s err=%s", r.returncode, (r.stderr or "")[:300])
        return None
    _announce("pdftotext")
    pages = r.stdout.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def _via_pypdfium2(pdf_path: Path, first: Optional[int], last: Optional[int]) -> list[str]:
    try:
        import pypdfium2 as pdfium
    except ImportError:
        _announce("none")
        return []
    _announce("pypdfium2")
    pdf = pdfium.PdfDocument(str(pdf_path))
    try:
        n = len(pdf)
        lo = max(1, first or 1)
        hi = min(n, last or n)
        out: list[str] = []
        for i in range(lo - 1, hi):
            page = pdf[i]
            tp = page.get_textpage()
            try:
                out.append(tp.get_text_bounded() or "")
            finally:
                tp.close()
                page.close()
        return out
    finally:
        pdf.close()


def pdf_pages_text(pdf_path: Path | str, first: Optional[int] = None, last: Optional[int] = None) -> list[str]:
    """Text of pages ``first``..``last`` (1-based, inclusive; default: all), one string per page.
    An empty list means no extractor could run -- callers treat that as "census unavailable"."""
    pdf_path = Path(pdf_path)
    if have_pdftotext():
        pages = _via_pdftotext(pdf_path, first, last)
        if pages is not None:
            return pages
    return _via_pypdfium2(pdf_path, first, last)


def pdf_page_text(pdf_path: Path | str, pno: int) -> str:
    pages = pdf_pages_text(pdf_path, pno, pno)
    return pages[0] if pages else ""
