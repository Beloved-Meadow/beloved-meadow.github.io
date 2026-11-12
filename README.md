# Beloved Meadow — website, first version

A static website with no accounts, tracking or forms. Fonts are self-hosted, and there are no running costs other than hosting, which can be free (for example Netlify, Cloudflare Pages or GitHub Pages).

## How it's published
The GitHub repo `Beloved-Meadow/beloved-meadow.github.io` holds the **source** (`src/`, `static/`, `build.py`).
On every push to `main`, `.github/workflows/pages.yml` runs `python3 build.py` and publishes `site/` to https://beloved-meadow.github.io.
New readings come in each week as a pull request (see `CLAUDE.md`). They only go live once you click **Merge**.

## Run it
```
python3 build.py                                   # rebuilds site/ from src/pages/
python3 -m http.server 8765 --directory site       # preview at http://localhost:8765
```
Edit text in `src/pages/*.html`. Page titles and descriptions are set in `build.py`. Styles are in `site/assets/style.css`.

To regenerate the family PDF after editing `families.html`, print `http://localhost:8765/families/` to `site/assets/downloads/beloved-meadow-what-is-god-like-family-companion.pdf` (Chrome → Print → Save as PDF, A4, without headers).

## What's in the site
- **Home**: the invitation, a "Meet Jesus" button, a direct link to the YouTube film and a bedtime question.
- **Meet Jesus**: an introduction to Jesus, and eight readings (John 14:8–9, Mark 10:13–16, Luke 19:1–10, Mark 14:32–36, Mark 10:46–52, John 21:15–17, John 10:11–15, John 20:24–29).
- **For Families**: a ten-minute companion to the film, with a print button and a free PDF. This is Evening 1 of the pack.
- **Family Conversation Pack** (`/families/conversation-pack/`): a page listing exactly what's in the pack, page by page, with four preview images. It is marked "Not on sale yet" and has no checkout.
- **For Churches**: a 15-minute session on Mark 4:35–41. The contact section is deliberately closed.
- **About**: what we believe and why we exist. No facts about the founder or team have been invented.

All Bible quotations come from the World English Bible (public domain). Retellings are labelled.

## The Family Conversation Pack (paid draft)
- Source: `pack/what-is-god-like-family-conversation-pack.html` (+ `pack/pack.css`)
- Ready-made PDF: `pack/Beloved-Meadow-What-Is-God-Like-Family-Conversation-Pack.pdf` (13 A4 pages)
- This folder is deliberately outside `site/`, so the paid pack is not public.
- Contents: a cover; an introduction; a listening guide for grown-ups; 5 evenings (Mark 6:34, Luke 15:20, John 11:32–35, Luke 23:33–34, Luke 24:36–39 + Matthew 28:20); a family poster; 8 big question cards; 6 prayer cards; a drawing page.
- To regenerate the PDF and preview images, open the HTML in Chrome and use Print → Save as PDF (A4, no margins, background graphics on). Add `#only=4` to the URL to see a single page.

## Other launch files
- `site/sitemap.xml`, `site/robots.txt` (fill in `SITE_URL` in `build.py` first, then run `python3 build.py`)
- `site/404.html`, and the share image `site/assets/img/share.png` (1200×630, source in `tools/share.html`)

## Launching (Netlify Drop, free)
1. Open https://app.netlify.com/drop.
2. Drag `beloved-meadow-site.zip` (or the `site` folder) onto it. The site is live straight away at a `*.netlify.app` address.
3. **Within an hour, click "Claim"** and create a free account. Otherwise the site disappears.
4. In Site settings, change the site name (for example `belovedmeadow`) or connect your own domain.
5. Send me the final address. I'll put it in `SITE_URL` and make a new zip, so the share image, canonical URLs and sitemap point to the right place. Then drag the new zip onto the same site (Deploys → drag and drop).

The zip contains only the public site. The paid pack (`pack/`) is not included.

## Needs your approval / input
1. **The Family Conversation Pack**: I wrote it myself, because the original was behind a ChatGPT sign-in. If you have an existing version, I'll merge the two. Before it can go on sale, you need to approve:
   - **the price** (suggested: €5–7 for a PDF)
   - **the sales channel** (suggested: Lemon Squeezy or Gumroad, which have no monthly fee and charge per sale, so they stay well under €50 a month)
   - **the content**, including the theology in Evening 4 and on the big question cards.

   The site has no live checkout.
2. **Contact for churches**: this stays closed until you provide a verified business address and an email address.
3. **Founder, team and organisation**: none of these details were supplied, so the About page contains none.
4. **Public launch**: choose a domain and hosting (Netlify or Cloudflare Pages, both free). Then fill in `SITE_URL` in `build.py`. That makes the canonical URLs, share image URLs and sitemap correct.
5. **Theology and wording**: please review the statement of belief on the About page and the explanations of the cross and resurrection.
6. **Ages**: the site is now written for children of every age. Each page includes tips for younger and older children.

## Proposed launch steps (no costs without your approval)
1. Read through the readings aloud with two or three families and one Sunday school leader, then revise.
2. Add a link to the site in the YouTube video description of *What Is God Like?*, pointing to /families/.
3. Send the church session to a few churches you know personally, once the contact route is open.
4. Each new film gets its own free family companion (the same format) and, if you choose, a paid pack.
