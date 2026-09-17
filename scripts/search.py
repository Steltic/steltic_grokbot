#!/usr/bin/env python3
"""Unified search CLI (spec + phase-2). stdlib + sqlite3. No vector DB.

Usage:
  search.py id <id> [--doc D] [--commentary] [--neighbors N] [--limit N]
  search.py exact_section <id>  [...]
  search.py eq | exact_equation <id>  [...]
  search.py table | exact_table <id>  [...]
  search.py fts "<query>" [--doc D] [--collection C] [--limit N] [--commentary]
  search.py keyword "<query>" [...]
  search.py command <name> [--limit N]

Lookup order (auto / miss fallback): exact section/eq/table, then FTS, then
keyword, then alias expansion. Results are verbatim extracts, never paraphrased.
Default: provision only (want_commentary false).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from retrieval import Corpus, format_cli_result, find_root  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__.strip())
        return 0
    mode = argv[0]
    rest = argv[1:]
    # flags may appear after the query; collect known flags
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--doc", default=None)
    parser.add_argument("--collection", default=None)
    parser.add_argument("--commentary", action="store_true")
    parser.add_argument("--neighbors", type=int, default=1)
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--root", default=None)
    parser.add_argument("--max-text", type=int, default=20000)
    parser.add_argument("--no-cache", action="store_true",
                        help="ignore the answer cache and re-run the lookup (it is keyed on the "
                             "index's fingerprint, so a rebuild already invalidates it)")
    # remaining positional = query tokens
    args, unknown = parser.parse_known_args(rest)
    query_parts = [u for u in unknown if not u.startswith("-")]
    query = " ".join(query_parts).strip()
    if not query:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    root = Path(args.root) if args.root else find_root()
    corpus = Corpus(root)
    corpus.use_cache = not args.no_cache
    result = corpus.search(
        type_=mode,
        query=query,
        doc=args.doc,
        want_commentary=bool(args.commentary),
        neighbors=args.neighbors,
        limit=args.limit,
        collection=args.collection,
    )
    out = format_cli_result(result, max_text=args.max_text)
    if result.get("cached"):
        out["cached"] = True          # the same answer a fresh lookup would give, from query_cache.sqlite
    print(json.dumps(out, ensure_ascii=False, indent=1))
    corpus.close()
    return 0 if result.get("found") else 1


if __name__ == "__main__":
    raise SystemExit(main())
