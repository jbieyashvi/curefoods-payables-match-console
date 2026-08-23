#!/usr/bin/env python3
"""Wrap the artifact-shaped sources into standalone documents for GitHub Pages.

payables-*.html are written for the Artifact host, which supplies the
<!doctype>/<head>/<body> skeleton at publish time, so they must NOT carry one of
their own. Served raw over Pages they would land in quirks mode. These copies add
the doctype (and nothing else) so the shared link renders exactly as the artifact
does. Regenerate with:  python3 .claude/build-share.py
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAIRS = [("payables-match-console.html", "console.html"),
         ("payables-design-system.html", "design-system.html")]
HEAD = '<!DOCTYPE html>\n<html lang="en">\n<meta charset="utf-8">\n'

for src_name, out_name in PAIRS:
    src = ROOT / src_name
    body = src.read_text(encoding="utf-8")
    if "<!doctype" in body.lower():
        sys.exit(f"{src_name} already carries a doctype — refusing to double-wrap")
    (ROOT / out_name).write_text(HEAD + body, encoding="utf-8")
    print(f"{src_name}  ->  {out_name}  ({len(HEAD)+len(body)} bytes)")
