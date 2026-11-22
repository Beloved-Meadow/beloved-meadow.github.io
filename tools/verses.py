#!/usr/bin/env python3
"""Print exact World English Bible verses from data/web/ (no network needed).

    python3 tools/verses.py "John 11:32-35"
    python3 tools/verses.py "Mark 10:46-52" --html   # <sup>n</sup> verse markup
"""
import json, re, sys, pathlib
DATA = pathlib.Path(__file__).resolve().parent.parent / "data" / "web"
ref = sys.argv[1]
m = re.fullmatch(r"\s*([1-3]?\s?[A-Za-z]+)\s+(\d+):(\d+)(?:-(\d+))?\s*", ref)
if not m:
    sys.exit("Use a reference like 'John 11:32-35'")
book, ch, v1, v2 = m.group(1).strip(), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
f = DATA / f"{book.lower()}.json"
if not f.exists():
    sys.exit(f"No local text for {book}. Available: {', '.join(p.stem for p in DATA.glob('*.json'))}")
verses = json.loads(f.read_text(encoding="utf-8"))["chapters"][ch]
html = "--html" in sys.argv
for v in range(v1, v2 + 1):
    t = verses[str(v)]
    print(f"<sup>{v}</sup>{t}" if html else f"{v} {t}")
