#!/usr/bin/env python3
"""Beloved Meadow static site builder.

Wraps each page body in src/pages/ with the shared header, footer and
<head> metadata, and writes the finished site to site/.
No dependencies beyond the Python standard library.

    python3 build.py
    python3 -m http.server 8080 --directory site
"""
from pathlib import Path
import html
import shutil

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "pages"
OUT = ROOT / "site"

# Set this once a domain is approved; used for canonical and share URLs.
SITE_URL = "https://beloved-meadow.github.io"  # e.g. "https://www.belovedmeadow.org" or "https://name.github.io/belovedmeadow"
# Path the site lives under. "/" for a domain or a name.github.io repo;
# "/belovedmeadow/" for a GitHub Pages project repo called belovedmeadow.
BASE_PATH = "/"
FILM_URL = "https://www.youtube.com/watch?v=0sQ-YYJqn94"

PAGES = [
    # (source, output, title, description, nav)
    ("home.html", "index.html",
     "Beloved Meadow — Come and meet Jesus",
     "Short Bible readings and conversations that help children get to know Jesus and talk to God honestly, with the grown-ups who love them.",
     "home"),
    ("meet-jesus.html", "meet-jesus/index.html",
     "Meet Jesus — Beloved Meadow",
     "Who is Jesus, why did he come, and what do his death and resurrection mean? A child-friendly introduction and four readings to share aloud.",
     "meet"),
    ("reading-1.html", "meet-jesus/what-is-god-like/index.html",
     "What is God like? A reading on John 14:8–9 — Beloved Meadow",
     "A three-minute reading for children: Philip asks to see the Father, and Jesus says, “He who has seen me has seen the Father.”",
     "meet"),
    ("reading-2.html", "meet-jesus/does-jesus-have-room-for-me/index.html",
     "Does Jesus have room for me? A reading on Mark 10:13–16 — Beloved Meadow",
     "A three-minute reading for children: the disciples try to send children away, and Jesus takes them in his arms.",
     "meet"),
    ("reading-3.html", "meet-jesus/can-jesus-still-love-me/index.html",
     "Can Jesus still love me when I’ve done something wrong? A reading on Luke 19:1–10 — Beloved Meadow",
     "A three-minute reading for children: Jesus stops under Zacchaeus’s tree, calls him by name and goes to his house.",
     "meet"),
    ("reading-4.html", "meet-jesus/can-i-talk-to-god-when-im-scared/index.html",
     "Can I talk to God when I’m scared? A reading on Mark 14:32–36 — Beloved Meadow",
     "A three-minute reading for children: Jesus prays honestly in Gethsemane, and children find words for their own fears.",
     "meet"),
    ("reading-5.html", "meet-jesus/can-i-ask-jesus-for-what-i-need/index.html",
     "Can I ask Jesus for what I need? A reading on Mark 10:46–52 — Beloved Meadow",
     "A three-minute reading for children: the crowd tells Bartimaeus to be quiet, but Jesus stands still and asks what he wants.",
     "meet"),
    ("reading-6.html", "meet-jesus/what-if-i-let-jesus-down/index.html",
     "What if I let Jesus down? A reading on John 21:15–17 — Beloved Meadow",
     "A three-minute reading for children: Peter denies Jesus three times, and the risen Jesus invites him back over breakfast.",
     "meet"),
    ("reading-7.html", "meet-jesus/why-did-jesus-die/index.html",
     "Why did Jesus die? A reading on John 10:11–15 — Beloved Meadow",
     "A three-minute reading for children: Jesus the good shepherd lays down his life for the sheep.",
     "meet"),
    ("reading-8.html", "meet-jesus/is-jesus-really-alive/index.html",
     "Is Jesus really alive? A reading on John 20:24–29 — Beloved Meadow",
     "A three-minute reading for children: Thomas doubts, and the risen Jesus comes back to meet him.",
     "meet"),
    ("reading-9.html", "meet-jesus/is-what-i-have-enough/index.html",
     "Is what I have enough for Jesus? A reading on John 6:5–13 — Beloved Meadow",
     "A three-minute reading for children: a boy’s five loaves and two fish feed a crowd of thousands in Jesus’ hands.",
     "meet"),
    ("reading-10.html", "meet-jesus/does-jesus-want-to-hear-thank-you/index.html",
     "Does Jesus want to hear “thank you”? A reading on Luke 17:11–19 — Beloved Meadow",
     "A three-minute reading for children: Jesus heals ten men, and one turns back to thank him.",
     "meet"),
    ("reading-11.html", "meet-jesus/is-jesus-stronger-than-my-storm/index.html",
     "Is Jesus stronger than my storm? A reading on Mark 4:35–41 — Beloved Meadow",
     "A three-minute reading for children: Jesus calms the wind and waves, and he is in the boat with his friends.",
     "meet"),
    ("reading-12.html", "meet-jesus/where-is-jesus-now/index.html",
     "Where is Jesus now? A reading on John 14:1–3 — Beloved Meadow",
     "A three-minute reading for children: Jesus promises to prepare a place and come again.",
     "meet"),
    ("families.html", "families/index.html",
     "For Families: a ten-minute companion to What Is God Like? — Beloved Meadow",
     "Watch the film, read Mark 6:34, talk through two open questions and try one thing together. Free to print or download.",
     "families"),
    ("conversation-pack.html", "families/conversation-pack/index.html",
     "What Is God Like? Family Conversation Pack — Beloved Meadow",
     "Five ten-minute evenings looking at Jesus to see what God is like, plus big question cards, prayer cards, a family poster and a drawing page.",
     "families"),
    ("churches.html", "churches/index.html",
     "For Churches: a 15-minute Sunday school session on Mark 4:35–41 — Beloved Meadow",
     "A complete, printable session for children of all ages: Jesus calms the storm. Leader script, discussion and an activity with ordinary supplies.",
     "churches"),
    ("404.html", "404.html",
     "Page not found — Beloved Meadow",
     "This page could not be found. Start with Meet Jesus or the home page.",
     "none"),
    ("about.html", "about/index.html",
     "About Beloved Meadow — what we believe and why we exist",
     "Beloved Meadow helps children get to know Jesus, grow to love him and discover that they can talk to God honestly.",
     "about"),
]

NAV = [
    ("home", "", "Home"),
    ("meet", "meet-jesus/", "Meet Jesus"),
    ("families", "families/", "For Families"),
    ("churches", "churches/", "For Churches"),
    ("about", "about/", "About"),
]

LOGO = """<svg viewBox="0 0 40 40" aria-hidden="true" focusable="false"><circle cx="20" cy="20" r="19" fill="#f9e9cf"/><circle cx="20" cy="17" r="7" fill="#e7b552"/><path d="M1.5 25c6-4 12-5 18.5-2.5S32 27 38.5 23.5V27a19 19 0 0 1-37 0z" fill="#2c6249"/><path d="M3.6 30c5.5-2.6 11-3 16.4-1.2S30.6 31.6 36.4 30A19 19 0 0 1 3.6 30z" fill="#1f4a36"/></svg>"""

TEMPLATE = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:site_name" content="Beloved Meadow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">{canonical}
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f4a36">
<meta name="google-site-verification" content="_PFoDyB4uulC66boVSy6Gq-it6-f0Gd4KbZgGBjN768">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{r}assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/style.css">
<script src="{r}assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{r}">{logo}<span>Beloved Meadow</span></a>
    <nav class="nav" aria-label="Main">
      <ul>{nav}</ul>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <h2>Beloved Meadow</h2>
      <p>Helping children get to know Jesus, grow to love him and discover that they can talk to God honestly.</p>
      <p class="note">Bible quotations are from the World English Bible (public domain). Retellings are labelled.</p>
    </div>
    <div>
      <h2>Explore</h2>
      <ul>
        <li><a href="{r}meet-jesus/">Meet Jesus</a></li>
        <li><a href="{r}families/">For Families</a></li>
        <li><a href="{r}churches/">For Churches</a></li>
        <li><a href="{r}about/">About</a></li>
      </ul>
    </div>
    <div>
      <h2>Watch</h2>
      <ul>
        <li><a href="{film}" rel="noopener">What Is God Like? on YouTube</a></li>
        <li><a href="https://www.youtube.com/@BelovedMeadowInt" rel="noopener">Beloved Meadow on YouTube</a></li>
      </ul>
      <p class="note">No accounts, no sign-ups. Nothing you pray, write or say is collected here.</p>
    </div>
  </div>
</footer>
</body>
</html>
"""


def build():
    # Static files (styles, fonts, images, downloads) live in static/ and are copied as-is.
    shutil.copytree(ROOT / "static", OUT, dirs_exist_ok=True)
    for src, out, title, desc, nav_key in PAGES:
        depth = out.count("/")
        r = "../" * depth
        if out == "404.html":
            r = BASE_PATH  # served at any path, so use absolute links
        body = (SRC / src).read_text(encoding="utf-8")
        body = body.replace("{r}", r).replace("{film}", FILM_URL)
        def current(key, href):
            if key != nav_key:
                return ""
            # Exact page gets "page"; a reading inside Meet Jesus gets "true".
            return ' aria-current="page"' if out == href + "index.html" else ' aria-current="true"'
        nav = "".join(
            f'<li><a href="{r or "./"}{href}"{current(key, href)}>{label}</a></li>'
            for key, href, label in NAV
        )
        canonical = ""
        if SITE_URL:
            path = out[:-len("index.html")] if out.endswith("index.html") else out
            canonical = f'\n<link rel="canonical" href="{SITE_URL}/{path}">\n<meta property="og:url" content="{SITE_URL}/{path}">'
        page = TEMPLATE.format(
            title=html.escape(title, quote=True),
            desc=html.escape(desc, quote=True),
            ogtype="website" if nav_key == "home" else "article",
            canonical=canonical,
            r=r or "./",
            logo=LOGO,
            nav=nav,
            body=body,
            film=FILM_URL,
            ogimg=(SITE_URL + "/" if SITE_URL else r or "./") + "assets/img/share.png",
        )
        target = OUT / out
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")
        print("built", out)


def extras():
    base = SITE_URL or "https://example.org"  # replace via SITE_URL before launch
    urls = "".join(
        f"  <url><loc>{base}/{out[:-len('index.html')]}</loc></url>\n" for _, out, *_ in PAGES if out != "404.html"
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n",
        encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    build()
    extras()
    (OUT / ".nojekyll").write_text("")  # GitHub Pages: serve files as-is
