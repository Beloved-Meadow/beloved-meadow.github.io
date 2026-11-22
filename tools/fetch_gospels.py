#!/usr/bin/env python3
"""Download the World English Bible (public domain) text of the Gospels into data/web/.
Run once locally; the weekly writer reads these files instead of the network."""
import json, time, urllib.request, pathlib
BOOKS = {"Matthew": 28, "Mark": 16, "Luke": 24, "John": 21, "Acts": 28}
out = pathlib.Path(__file__).resolve().parent.parent / "data" / "web"
out.mkdir(parents=True, exist_ok=True)
for book, n in BOOKS.items():
    data = {"book": book, "translation": "World English Bible (public domain)", "chapters": {}}
    for ch in range(1, n + 1):
        url = f"https://bible-api.com/{book.lower()}+{ch}?translation=web"
        for attempt in range(6):
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    d = json.load(r)
                break
            except Exception as e:
                time.sleep(8 * (attempt + 1))
        else:
            raise SystemExit(f"failed {url}")
        data["chapters"][str(ch)] = {str(v["verse"]): " ".join(v["text"].split()) for v in d["verses"]}
        time.sleep(2.2)
    (out / f"{book.lower()}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(book, n, "chapters")
