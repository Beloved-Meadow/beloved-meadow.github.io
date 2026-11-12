# Beloved Meadow — guide for Claude

Beloved Meadow helps children get to know Jesus, grow to love him, and discover that they can talk to God honestly. Everything here serves one question: **what does this help a child see about Jesus?** Seek first his Kingdom and his righteousness (Matthew 6:33). The goal is never content volume. It is children and families meeting Jesus in Scripture.

## Project layout
- `src/pages/*.html` — page bodies (no `<head>`). `{r}` = relative root, `{film}` = film URL.
- `build.py` — the `PAGES` list (source, output path, title, description, nav) + shared template. Run `python3 build.py` → writes `site/`.
- `site/` — build output, **never edit by hand** and never commit (GitHub Actions builds it).
- The paid Family Conversation Pack is **not** in this repo and must never be added.

## Weekly task: add one new Meet Jesus reading
Open **one pull request per week** with exactly one new reading. Never push to `main`; a human reviews and merges.

1. Read `src/pages/meet-jesus.html` and every existing `src/pages/reading-*.html` first. Do not repeat a passage or a question already covered.
2. Pick a passage from the Gospels (or one that clearly shows Jesus) and a real question a child asks. Prefer moments where Jesus *does* something.
3. Fetch the exact World English Bible text: `curl -s "https://bible-api.com/<book>+<ch>:<v>-<v>?translation=web"`. Quote it **verbatim**, keep verse numbers as `<sup>`. Never quote from memory.
4. Create `src/pages/reading-N.html` by copying the structure of the latest reading:
   - header: `Meet Jesus · Reading N of N`, `h1` = the child's question, meta (reference, "About 3 minutes aloud", "For children of every age"), print button
   - **A moment you might know** — a concrete everyday moment a child recognises
   - **From the Bible** — short labelled *Retelling* for context + the Bible text block
   - **Wonder together** — 2 questions with `.pause` cues; let the child notice before explaining
   - **Something to carry today** — one sentence about Jesus
   - **If you'd like to respond** — borrowed words / own words / silence (always optional, private)
   - **For the grown-up** (`details.grownup`) — what this shows about Jesus, listening tips, care notes
   - pager (previous ↔ next) + print footer
5. Update: previous reading's "next" link and every reading's "of N" count; the list in `meet-jesus.html` (and counts in its text); the `PAGES` list in `build.py` (title ≤ 70 chars, description ≤ 160 chars). Optionally add a card to `home.html`.
6. Run `python3 build.py` and check the output builds without errors and all internal links resolve.
7. PR title: `New reading: <question> (<reference>)`. PR body: the passage, why it was chosen, and the full child-facing text so the reviewer can read it in the PR.

## Editorial standard (non-negotiable)
- Warm, precise British English that sounds natural read aloud in ~3 minutes (≈ 400–500 words child-facing).
- **Only attribute words to Jesus when they come from the cited passage.** Label every retelling or paraphrase.
- Accurate references. Never invent details about the biblical text.
- Christ-centred and gospel-faithful: who Jesus is, why he came, his death and resurrection, forgiveness, hope, life with God. Not moralising — the story shows Jesus first; any response flows from his grace.
- Handle fear, doubt, grief and wrongdoing with care. Don't promise outcomes God hasn't promised. Include safeguarding wording when a reading touches harm or fear.
- Prayer is always a choice: aloud, own words, or quietly. Never collect or ask for a child's responses.
- Read it back as a child, a parent and a Sunday school leader; revise anything vague, preachy or too polished.
- No new third-party scripts, trackers, forms or paid services.
