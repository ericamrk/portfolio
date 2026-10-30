import re, os
p = os.path.join(os.path.dirname(__file__), '..', 'site', 'index.html')
s = open(p).read()
def rep(a, b):
    global s
    assert a in s, 'MISSING: ' + a[:80]; s = s.replace(a, b, 1)
def cut(a_mark, b_mark, new):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a); s = s[:a] + new + s[b:]

# ---------- fonts & display type ----------
s = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/css2\?[^"]+">',
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..700&family=Hanken+Grotesk:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Nanum+Pen+Script&display=swap">', s, count=1)
rep('--f-display: "Bodoni Moda", "Didot", "Bodoni 72", Georgia, serif;',
    '--f-display: "Archivo", "Helvetica Neue", Arial, sans-serif;\n  --f-hand: "Nanum Pen Script", "Bradley Hand", cursive;')
s = re.sub(r'font: 400 ([^;]*?)var\(--f-display\);', r'font: 300 \1var(--f-display); font-stretch: 112%;', s)

# ---------- hero CSS ----------
a = s.index('.hero .wrap {'); b = s.index('.hero .lead {')
s = s[:a] + """.hero .wrap { display: grid; gap: clamp(18px, 3vw, 36px); padding-block: clamp(18px, 3vw, 36px) clamp(28px, 4vw, 52px); }
.hero-top { display: flex; justify-content: space-between; gap: 16px; color: var(--muted); border-bottom: 1px solid var(--line); padding-bottom: 10px; }
.poster { margin: 0; font: 200 clamp(50px, 10.4vw, 160px)/1 var(--f-display); font-stretch: 112%; letter-spacing: -.035em; display: grid; gap: .06em; }
.poster .ln { display: flex; align-items: center; justify-content: space-between; gap: .1em .14em; flex-wrap: wrap; }
.poster .chip { flex: none; height: .58em; padding: 0; border: 0; background: var(--hatch); cursor: pointer; box-shadow: var(--shadow); transition: transform .4s cubic-bezier(.22,1,.36,1); }
.poster .chip.sm { height: .4em; }
.poster .chip img { display: block; height: 100%; width: auto; max-width: none; }
.poster .chip:hover, .poster .chip:focus-visible { transform: translateY(-.05em) rotate(-2.5deg); }
.hand { font: 400 clamp(22px, 2vw, 30px)/1 var(--f-hand); letter-spacing: 0; color: var(--ink); }
.poster .hand { align-self: flex-end; padding-bottom: .5em; white-space: nowrap; }
.hero-row { display: grid; grid-template-columns: minmax(0, .85fr) minmax(0, 1.15fr); gap: clamp(24px, 4vw, 64px); align-items: center; }
.ring-note { position: absolute; left: 2%; top: 0; z-index: 2; display: flex; align-items: flex-start; gap: 4px; transform: rotate(-5deg); pointer-events: none; }
.ring-note svg { width: 46px; height: 40px; fill: none; stroke: var(--ink); stroke-width: 1.4; stroke-linecap: round; margin-top: 10px; }
""" + s[b:]
rep('.ring-stage { position: relative; height: clamp(300px, 38vw, 440px);', '.ring-stage { position: relative; height: clamp(280px, 32vw, 400px);')
rep('  .hero .wrap, .about-grid, .contact-sheet { grid-template-columns: minmax(0, 1fr); }', '  .hero-row, .about-grid, .contact-sheet { grid-template-columns: minmax(0, 1fr); }')

# ---------- folder tabs, section numbers, paperclip, inbox cover, stack heads/video ----------
rep('/* ---------- Case study sheet ---------- */', """/* ---------- Folder tabs on the right edge ---------- */
.rail { display: none; }
@media (min-width: 1200px) {
  .rail { position: fixed; right: 0; top: 50%; transform: translateY(-50%); z-index: 15; display: grid; gap: 6px; }
  .rail a {
    writing-mode: vertical-rl; display: flex; gap: 14px; align-items: center; padding: 16px 9px 20px 8px;
    background: var(--paper); border: 1px solid var(--line); border-right: 0; border-radius: 10px 0 0 10px; box-shadow: var(--shadow);
    color: var(--muted); text-decoration: none; font-family: var(--f-mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase;
    transform: translateX(7px); transition: transform .25s ease, color .25s ease;
  }
  .rail a b { font-weight: 500; color: var(--ink); }
  .rail a:hover, .rail a.on { transform: none; color: var(--ink); }
  .rail a.on { border-color: var(--ink); }
  .wrap { padding-right: max(64px, env(safe-area-inset-right, 0px)); }
}
.band-head h2 .num { font: 400 11px/1 var(--f-mono); letter-spacing: .08em; color: var(--muted); vertical-align: top; margin-right: 12px; }
.contact-sheet { position: relative; }
.contact-sheet .clip { position: absolute; left: 28px; top: -26px; width: 26px; height: 64px; fill: none; stroke: var(--muted); stroke-width: 2; stroke-linecap: round; transform: rotate(-9deg); }
.addr .hand { margin-left: 6px; transform: rotate(-3deg); }
.inbox { aspect-ratio: 4 / 5; max-width: 100%; background: var(--paper); border: 1px solid var(--line); display: grid; align-content: start; overflow: hidden; }
.card.wide .inbox { aspect-ratio: 16 / 10; }
.inbox-top { display: flex; justify-content: space-between; padding: 10px 12px; border-bottom: 1px solid var(--line); color: var(--muted); }
.inbox-row { display: grid; gap: 3px; padding: 12px; border-bottom: 1px solid var(--line); }
.inbox-row b { font: 600 12px/1.2 var(--f-body); }
.inbox-row span { font-size: 13px; line-height: 1.35; color: var(--ink); }
.inbox-row:first-of-type { background: var(--hatch); }
.inbox-row i { font: 400 10px/1 var(--f-mono); color: var(--muted); font-style: normal; letter-spacing: .05em; text-transform: uppercase; }
.stack .head { grid-column: 1 / -1; display: flex; justify-content: space-between; align-items: baseline; gap: 12px; border-top: 1px solid var(--line); padding-top: 12px; margin-top: 8px; }
.stack .head h4 { margin: 0; font: 300 22px/1.2 var(--f-display); font-stretch: 112%; }
.stack video { display: block; width: 100%; height: auto; background: #000; }

/* ---------- Case study sheet ---------- */""")

# ---------- hero HTML ----------
cut('  <section class="hero" aria-label="Introduction">', '  <section id="work"', """  <section class="hero" aria-label="Introduction">
    <div class="wrap">
      <div class="hero-top mono"><span>Graphic designer · Toronto</span><span>Portfolio (2026)</span></div>
      <h1 class="poster" id="poster" aria-label="Rongke Erica Ma"></h1>
      <div class="hero-row">
        <div>
          <p class="lead">Campaigns, HTML email, print and motion for fashion and lifestyle brands. I trained in fashion design and take every brief from concept to production-ready files.</p>
          <div class="jump" role="group" aria-label="Jump to a type of work">
            <button type="button" data-jump="campaign">Campaign<b data-count="campaign"></b></button>
            <button type="button" data-jump="email">HTML email<b data-count="email"></b></button>
            <button type="button" data-jump="web">Landing page<b data-count="web"></b></button>
            <button type="button" data-jump="pdf">PDF &amp; print<b data-count="pdf"></b></button>
            <button type="button" data-jump="motion">Motion<b data-count="motion"></b></button>
            <button type="button" data-jump="runway">Runway<b data-count="runway"></b></button>
          </div>
        </div>
        <div class="ring-stage" id="ringStage" tabindex="0" role="region" aria-roledescription="carousel" aria-label="Selected projects. Use arrow keys to turn, Enter to open.">
          <div class="ring-note" aria-hidden="true"><span class="hand">drag to spin</span><svg viewBox="0 0 46 40"><path d="M2 6c14-4 30 2 34 22"/><path d="M29 22l7 7 5-9"/></svg></div>
          <div class="ring" id="ring"></div>
          <div class="ring-caption mono"><span>Drag to turn · click to open</span><output id="ringOut" aria-live="polite"></output></div>
        </div>
      </div>
    </div>
  </section>

""")
rep("""        <h2>Selected work</h2>""", """        <h2><span class="num">001</span>(Selected work)</h2>""")
rep("""<div class="band-head"><h2>About</h2>""", """<div class="band-head"><h2><span class="num">002</span>(About)</h2>""")
rep("""      <div class="contact-sheet">
        <div>
          <span class="mono" style="color:var(--muted)">Contact</span>
          <h2>Let's talk.</h2>""", """      <div class="contact-sheet">
        <svg class="clip" viewBox="0 0 26 64" aria-hidden="true"><path d="M8 18v32a5 5 0 0 0 10 0V10a8 8 0 0 0-16 0v40a11 11 0 0 0 22 0V20"/></svg>
        <div>
          <span class="mono" style="color:var(--muted)">003 · Contact</span>
          <h2>(Let's talk)</h2>""")
rep("""            <button class="btn" type="button" id="copy">Copy email</button>""", """            <button class="btn" type="button" id="copy">Copy email</button>
            <span class="hand" aria-hidden="true">say hi!</span>""")
rep("""          <a class="btn ghost" href="#contact" aria-disabled="true">LinkedIn · add link</a>""", """          <a class="btn ghost" href="https://www.linkedin.com/in/rongke-ma-b74943298" target="_blank" rel="noopener">LinkedIn ↗</a>""")
rep("""<main id="top">""", """<nav class="rail" aria-label="Sections">
  <a href="#work" data-sec="work"><b>001</b><span>Selected work</span></a>
  <a href="#about" data-sec="about"><b>002</b><span>About</span></a>
  <a href="#contact" data-sec="contact"><b>003</b><span>Contact</span></a>
</nav>

<main id="top">""")

# ---------- content ----------
rep("""        { src: I + 'old-web-sandwich.webp', cap: 'Web banner and sandwich board' }
      ] },""", """        { src: I + 'old-neandertal.webp', cap: 'Neandertal, social media' },
        { src: I + 'old-web-sandwich.webp', cap: 'Web banner and sandwich board' }
      ] },""")
rep("summary: 'Launch visuals for the season\\'s new-arrival brands, plus posters,", "summary: 'Launch visuals and social posts for the season\\'s new-arrival brands, plus posters,")
rep("deliverables: 'Brand launch visuals, posters, gift card,", "deliverables: 'Brand launch visuals, social media posts, posters, gift card,")
cut("    { id: 'neandertal',", "    { id: 'tuke',", "")
cut("    { id: 'dkr-fall',", "    { id: 'wdlt',", """    { id: 'dkr-emails', title: 'Email campaigns', client: 'DKR & Co.', year: '2026',
      inbox: [
        ['Spring/Summer 2026 catalogues are now available to download', 'Catalogue launch'],
        ['The Casual Elegance Collection: weightless, vibrant', 'Collection story'],
        ['Fall Is Here', 'Sweater collections'],
        ['The Original Sherpa, now in stock', 'Product drop']
      ],
      summary: 'Mailchimp campaigns for a wholesale apparel brand: catalogue launches, collection stories and product drops sent to retail buyers.',
      cats: ['email','campaign'], role: 'Design and build in Mailchimp',
      deliverables: 'Email campaigns, header graphics, product modules', tools: 'Mailchimp, Canva, Photoshop',
      brief: 'Keep retail buyers ordering between catalogues with short, product-led emails that work on a phone.',
      state: 'Screenshots coming',
      links: [
        { label: 'SS26 catalogues · email A', href: 'https://mailchi.mp/d0a7b6002845/springsummer-2026-catalogues-are-now-available-digitally-to-download-8760118' },
        { label: 'SS26 catalogues · email B', href: 'https://mailchi.mp/eab7a2d6759d/springsummer-2026-catalogues-are-now-available-digitally-to-download-8759873' },
        { label: 'The Casual Elegance Collection', href: 'https://mailchi.mp/d55317452356/the-casual-elegance-collection-weightless-vibrant-8759442' }
      ] },

""")
G = lambda f, c: "        { src: I + '%s.webp', cap: '%s' }," % (f, c)
runway = [
 "        { head: 'Mass Exodus 2024', note: 'TMU graduate show' },",
 G('rw-mx-lineup', 'Finale line-up'),
 "        { video: 'files/metamorphosis-runway.mp4', src: I + 'rw-mx-clip-poster.webp', cap: 'Runway clip' },",
 G('rw-mx-01', 'Satin gown with mirrored orb'), G('rw-mx-02', 'Teal cut-out dress'), G('rw-mx-03', 'White collar cape, feather bodice'),
 G('rw-mx-04', 'Feather-hem bodysuit'), G('rw-mx-05', 'Black cut-out dress'),
 "        { head: 'Fashion Art Toronto', note: 'Selected showcase' },",
 G('rw-fat-wide', 'The runway'), G('rw-fat-01', 'Satin gown with mirrored orb'), G('rw-fat-02', 'Teal cut-out dress'),
 G('rw-fat-03', 'Teal cut-out dress, front'), G('rw-fat-04', 'Satin gown, front'), G('rw-fat-05', 'Feather-hem bodysuit'),
 G('rw-fat-06', 'White cape and feather bodysuit'), G('rw-fat-07', 'White cape, back view'), G('rw-fat-08', 'Satin gown with headpiece'),
 G('rw-fat-09', 'Teal dress with cut-outs'), G('rw-fat-detail-01', 'Detail: the mirrored orb'), G('rw-fat-detail-02', 'Detail: the orb in motion'),
 G('rw-fat-10', 'Teal dress on the runway'), G('rw-fat-11', 'Feather bodysuit on the runway'),
 "        { head: 'Backstage & fittings' },",
 G('rw-bts-wide', 'Backstage before the show'), G('rw-bts-01', 'Satin gown, backstage portrait'), G('rw-bts-02', 'Feather bodysuit, backstage'),
 G('rw-bts-03', 'Black dress, backstage'), G('rw-bts-04', 'Feather bodysuit, backstage'), G('rw-bts-05', 'Satin gown and orb, backstage'),
 G('rw-bts-06', 'Looks lined up backstage'), G('rw-bts-orb', 'Holding the orb'), G('rw-fit-01', 'Fitting in the studio'), G('rw-fit-02', 'Fitting in the studio'),
]
rep("""    { id: 'meta-editorial',""", """    { id: 'runway', title: 'Metamorphosis on the runway', client: 'Mass Exodus 2024 · Fashion Art Toronto', year: '2024',
      cover: I + 'rw-fat-01.webp',
      summary: 'The collection on the runway at TMU\\'s Mass Exodus 2024 and at Fashion Art Toronto, where it was selected for an additional showcase.',
      cats: ['runway'], role: 'Designer', deliverables: 'Runway collection', tools: 'Design, pattern making, construction',
      gallery: [
""" + "\n".join(runway).rstrip(',') + """
      ] },

    { id: 'meta-editorial',""")

# ---------- card cover: inbox ----------
rep("""      ${p.cover ? `<div class="shot">""", """      ${p.inbox ? `<div class="inbox"><div class="inbox-top mono"><span>Inbox</span><span>${p.client}</span></div>${p.inbox.map(([subj, kind]) => `<div class="inbox-row"><b>${p.client}</b><span>${subj}</span><i>${kind}</i></div>`).join('')}</div>` : p.cover ? `<div class="shot">""")

# ---------- stack: heads + video ----------
rep("""    const items = g.map(x => {
      const [w, h] = DIMS[x.src] || [4, 5], r = w / h;
      return { ...x, w, h, kind: r > 1.15 ? 'span' : 'half' };
    });""", """    const items = g.map(x => {
      if (x.head) return { ...x, kind: 'head' };
      const [w, h] = DIMS[x.src] || [4, 5], r = w / h;
      return { ...x, w, h, kind: r > 1.15 ? 'span' : 'half' };
    });
    let n = 0;""")
rep("""    return `<div class="stack">${items.map((x, i) => `<figure class="${x.kind}"><img src="${x.src}" alt="${attr(p.title + ': ' + x.cap)}" width="${x.w}" height="${x.h}"${i > 1 ? ' loading="lazy"' : ''} decoding="async"><figcaption class="mono">${pad2(i + 1)} · ${x.cap}</figcaption></figure>`).join('')}</div>`;""",
"""    return `<div class="stack">${items.map((x, i) => {
      if (x.kind === 'head') return `<div class="head"><h4>${x.head}</h4>${x.note ? `<span class="mono" style="color:var(--muted)">${x.note}</span>` : ''}</div>`;
      n++;
      const media = x.video
        ? `<video src="${x.video}" poster="${x.src}" width="${x.w}" height="${x.h}" controls muted playsinline loop preload="none" aria-label="${attr(p.title + ': ' + x.cap)}"></video>`
        : `<img src="${x.src}" alt="${attr(p.title + ': ' + x.cap)}" width="${x.w}" height="${x.h}"${i > 2 ? ' loading="lazy"' : ''} decoding="async">`;
      return `<figure class="${x.kind}">${media}<figcaption class="mono">${pad2(n)} · ${x.cap}</figcaption></figure>`;
    }).join('')}</div>`;""")

# ---------- poster headline + rail scroll-spy ----------
rep("  /* ---------------- Cards ---------------- */", """  /* ---------------- Poster headline: name set with small work images ---------------- */
  const POSTER = [
    ['(Rongke', { id: 'uniqlo-ad' }, ')', { id: 'meta-editorial', sm: 1 }],
    [{ id: 'dkr-catalogue' }, '(Erica)', { id: 'momore', sm: 1 }, { id: 'uniqlo-email' }],
    ['(Ma', { id: 'runway' }, ')', { hand: 'fashion → graphic design' }]
  ];
  $('#poster').innerHTML = POSTER.map(line => `<span class="ln">${line.map(t => {
    if (typeof t === 'string') return `<span aria-hidden="true">${t}</span>`;
    if (t.hand) return `<span class="hand" aria-hidden="true">${t.hand}</span>`;
    const p = PROJECTS.find(x => x.id === t.id); if (!p?.cover) return '';
    const [w, h] = DIMS[p.cover] || [4, 5];
    return `<button type="button" class="chip${t.sm ? ' sm' : ''}" data-open="${p.id}" aria-label="Open ${p.title}"><img src="${p.cover}" alt="" width="${w}" height="${h}"></button>`;
  }).join('')}</span>`).join('');

  /* ---------------- Cards ---------------- */""")
rep("  cards.addEventListener('click', e => { const c = e.target.closest('.card'); if (c) openCase(c.dataset.id); });",
"""  cards.addEventListener('click', e => { const c = e.target.closest('.card'); if (c) openCase(c.dataset.id); });
  $('#poster').addEventListener('click', e => { const c = e.target.closest('[data-open]'); if (c) openCase(c.dataset.open); });
  const railLinks = [...document.querySelectorAll('.rail a')];
  const spy = new IntersectionObserver(entries => entries.forEach(en => {
    if (en.isIntersecting) railLinks.forEach(a => a.classList.toggle('on', a.dataset.sec === en.target.id));
  }), { rootMargin: '-45% 0px -50% 0px' });
  ['work', 'about', 'contact'].forEach(id => spy.observe(document.getElementById(id)));""")

open(p, 'w').write(s); print('patched')
