# Portfolio site — working notes

Live draft: claude.ai artifact "Rongke Ma Portfolio" (Fo3jD4cxuYpVSbEABNqpH3). Target: Sun Life Digital Graphic Designer (JR00129134), posting closes Nov 6, 2026.

## How the site is built
- One HTML page + `images/*.webp` + `files/`. Links to our own files (`files/...`, `images/...`) open in an in-page viewer, because relative links opened in a new tab don't work from the artifact: HTML is fetched into an iframe (srcdoc + <base>), PDFs show as page images from `files/pages/<name>-NN.webp` (PDF_PAGES map in the script; render with pdftoppm when adding a PDF), images show full size.
- All project content lives in the `PROJECTS` array near the top of the script. Gallery items: `{src, cap}`, `{head, note}` for a section heading, `{video, src: poster, cap}`, `{anim}` autoplay muted loop. Email collections can use `inbox: [[subject, type]]` as a typographic cover.
- Case study: text on top, images below. If a gallery has `{head}` items, each head becomes a folder tab (colour-coded paper folders, ref: Arkivin tabs; tabs wrap onto extra rows on narrow screens); only one section shows at a time. `{sub}` = subheading inside a folder. `{mail, src: half-crop}` = email preview showing the top half with a fade and a 'View the full email' button. Landscape full width, portraits two-up, a lone portrait centred.
- Empty Role / Approach / Production blocks are hidden (never show notes to self). There is no Outcome block any more.
- `tools/update_dims.py` merges local image sizes into the page's DIMS blob (keeps entries for images other sessions added). Larger edits go in `tools/patch_*.py` scripts.
- Look: poster headline "(Rongke) (Erica) (Ma)" in light expanded Archivo with clickable work images between the words (POSTER array), handwritten notes (Nanum Pen Script), folder tabs on the right edge (001 work / 002 about / 003 contact), paperclip on the contact sheet, mono labels, grey wall + paper cards.
- Index: Digital / Print / Fashion design (collection, runway, editorial). Empty categories and hero buttons hide; filters scroll to first match.
- The artifact only serves standard web types: .vtt caption files are refused (use .txt or burn in).
- On a normal website (top-level page), links to HTML/PDF files open natively in a new tab; only inside the Claude viewer (framed) do they open in the in-page viewer, with in-page # links handled inside the frame (they used to navigate the frame to claude.ai and get blocked).
- Two sessions publish to this artifact: before publishing, read the live version and build on it.

## Decisions
- WDLT117 = one project "Visual marketing for a concept store", folders: New arrivals / Window & storefront (mock-up, installed window, street view, sandwich board) / Promotions & holidays / Social media · fragrance (Neandertal incl. "Them", + Ô series).
- Personal project = exhibition posters only. Her perfume packaging is not WDLT117.
- Covers: Light rain ad = landscape version; Editorial pulls = glow-forest shot.
- Mo&More = Mardi Mercredi web banner + in-store poster.
- Metamorphosis: Collection = five look folders (Look 1 · Incubation silver orb gown / 2 · Emergence Evolution teal / 3 · Awakening white cape + feather bodysuit / 4 · Ascension feather skirt / 5 · Eternity in a Moment black), concept as Brief, credits block, each look's text + model credit (`{text, credit}` item) at the end of its folder; cover = orb close-up (meta-l1-orb); Runway with folders Mass Exodus 2024 (line-up, looks, line-up after the show, two before-the-show shots; no video) and Fashion Art Toronto (runway, details, Backstage sub-section; duplicate cape back view removed; project cover rw-fat-05); Editorial pulls.
- DKR emails: folders FW26 Essentials / FW26 Fleece / FW26 Market Week (half-length previews) + live mailchi.mp links.
- Hockey project removed (Oct 30). Retail email's +16% CTR / +12% conversion now in its summary.
- Contact: email, Instagram @erica_rk, LinkedIn linkedin.com/in/rongke-ma-b74943298. No phone. Résumé button removed until a résumé PDF exists.

## Waiting on
- Updated résumé PDF (then add the button back).
- Originals to replace old-portfolio page crops: retail email ("New Season, New Styles", client/year unknown), exhibition posters, TUKE content calendar, Metamorphosis collection pages.
- Which live mailchi.mp link matches which email.
- DKR email open/click rates if available.
- Live site: https://rongke-ma.vercel.app (use this, not the Claude artifact link, for interviewers).
- Hosting: GitHub repo ericamrk/portfolio (branch main, static site at repo root; `_source/` holds the editable page, tools and notes, excluded from deploy by .vercelignore) → Vercel imports it and redeploys on every push. To update: edit site/index.html, run `python3 tools/build_deploy.py`, copy deploy/rongke-ma-portfolio/* into the repo root, also copy site/index.html to _source/artifact-index.html, commit, push. Republish the Claude preview too.

## Picking this up in a new chat
- The published artifact holds every file. Read it with the Artifact tool (`read` with the URL, `scope: "files"` to list, `paths` to download) and republish to the same URL.

## First Cover (self-initiated, for the Sun Life application) — v1 done Oct 29
On the site as the wide first card (id `first-cover`), with folder tabs Brand / Campaign / HTML email / Landing page / Interactive PDF / 15s video; also a chip in the poster headline's third line. Site files: `images/fc-*.webp`, `files/first-cover-email.html` (+ `files/images/fc-mark.png`), `files/first-cover-landing.html`, `files/first-cover-plan-guide.pdf` (+ `files/pages/first-cover-guide-NN.webp`), `files/first-cover-15s.mp4`.
- Idea: "the firsts list" — insurance as the adult first nobody celebrates; the checkbox is the brand. Campaign line "First lease. First paycheque. First cover." Brand line "Your first plan, in plain words."
- Lead story: turning 25 in Ontario (parent's plan usually ends at 25; OHIP+ ends on the 25th birthday). Second story: freelance/contract with no group plan.
- Product (fictional, illustrative prices): First Cover Starter = prescriptions + virtual care + travel medical included ($34), tick-on modules Dental $19 / Mind $16 / Body $11 / Vision $7; quote form flags the free Canadian Dental Care Plan (<$90k family net income, no dental insurance).
- Colour: paper #F7F3EC, white, ink #17251F, ink-muted #4A5A52, spruce #1E5A47 (brand), mint #D5EBDF, coral #EA5C3E (the tick, never text), line #D9D2C5, field-border #7A857F, error #A31D2E. Type: Fraunces 600 / Atkinson Hyperlegible / Atkinson Hyperlegible Mono.
- Artifacts: brand system "First Cover" (Design System, 7ApnJUo2DAHBhTtC6tHvuT); campaign canvas "First Cover Campaign" (UEnj4LANLoT95MKx18sT11); landing page "First Cover" (8NQ6qFxzUbXTvhJ2ZYtq53).
- Known gaps: the PDF and video were rendered with stand-in fonts (Charter + DejaVu Sans); re-render once Erica uploads Fraunces / Atkinson Hyperlegible font files, or rebuild the PDF in InDesign. Video has no audio track (captions carry the VO script).
