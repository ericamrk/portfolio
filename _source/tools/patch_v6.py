import os
p = os.path.join(os.path.dirname(__file__), '..', 'site', 'index.html'); s = open(p).read()
def rep(a, b):
    global s
    assert a in s, 'MISSING: ' + a[:80]; s = s.replace(a, b, 1)
def cut(a_mark, b_mark, new):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a); s = s[:a] + new + s[b:]
G = lambda f, c: "        { src: I + '%s.webp', cap: '%s' }," % (f, c)
H = lambda h: "        { head: '%s' }," % h
A = lambda f, c: "        { anim: 'files/%s.mp4', src: I + '%s.webp', cap: '%s' }," % (f, f, c)
wdlt = [H('New arrivals'), A('wdlt-na-anim', 'New arrivals, animated post'), A('wdlt-ottolinger-anim', 'Ottolinger, animated post'),
 G('wdlt-na-poster', 'New arrivals poster'), G('wdlt-heliot-emil', 'Heliot Emil'), G('wdlt-rombaut', 'Rombaut'), G('wdlt-published-by', 'Published By'),
 H('Window & storefront'), G('wdlt-window-mockup', 'Window design, mock-up'), G('wdlt-sandwich', 'Sandwich board on the street'),
 H('Promotions & holidays'), G('wdlt-promo-exclusive', 'Exclusive promo, social'), G('wdlt-promo-poster', 'Exclusive promo, poster'),
 G('wdlt-christmas', 'Christmas'), G('wdlt-boxing-week', 'Boxing Week early access'), G('wdlt-cny', 'Chinese New Year'),
 G('wdlt-qixi', "Chinese Valentine\\'s Day, story"), G('wdlt-hours', 'Business hours, story'), G('wdlt-wanderlust-story', 'Wanderlust, story'),
 H('Social media · fragrance'), G('wdlt-nea-cover', 'Neandertal, launch'), G('wdlt-nea-brand', 'Neandertal, brand story'),
 G('wdlt-nea-light', 'Neandertal, Light'), G('wdlt-nea-dark', 'Neandertal, Dark'), G('wdlt-nea-us', 'Neandertal, Us'),
 G('wdlt-o-founders', 'Ô, the founders'), G('wdlt-o-madame-x', 'Ô, Madame X'), G('wdlt-o-soigne', 'Ô, Soigné'),
 G('wdlt-o-fonteyn', 'Ô, Fonteyn'), G('wdlt-o-bullshit', 'Ô, Bullshit candle'), G('wdlt-o-them', 'Ô, Them'), G('wdlt-o-candles', 'Ô, candle range')]
cut("    { id: 'wdlt',", "    { id: 'personal',", """    { id: 'wdlt', title: 'Visual marketing for a concept store', client: 'WDLT117 · Yorkville', year: '2022–23',
      cover: I + 'wdlt-na-poster.webp',
      summary: 'New-arrival launches, window and street signage, seasonal promotions and fragrance social posts for a multi-brand concept store.',
      cats: ['campaign','print'], role: 'Visual marketing designer',
      deliverables: 'Animated posts, posters, window graphics, sandwich board, promotions, Instagram stories', tools: 'Photoshop, Illustrator',
      brief: 'Introduce each new-arrival brand in the store\\'s own voice, in store, on the street and on Instagram.',
      gallery: [
""" + "\n".join(wdlt).rstrip(',') + """
      ] },

""")
cut("    { id: 'personal',", "    { id: 'tuke',", """    { id: 'personal', title: 'Exhibition posters', client: 'Personal project', year: '',
      cover: I + 'old-posters.webp',
      summary: 'A self-directed poster series for art and environmental exhibitions.',
      cats: ['print'], role: 'Concept and design', deliverables: 'Poster series', tools: 'Photoshop, Illustrator',
      gallery: [{ src: I + 'old-posters.webp', cap: 'Exhibition posters' }] },

""")
rep("""        ['Spring/Summer 2026 catalogues are now available to download', 'Catalogue launch'],
        ['The Casual Elegance Collection: weightless, vibrant', 'Collection story'],
        ['Fall Is Here', 'Sweater collections'],
        ['The Original Sherpa, now in stock', 'Product drop']""", """        ['The F/W26 Essentials Collection, now in stock', 'Collection launch'],
        ['Ultra-soft brushed fleece, now in stock', 'Restock'],
        ['Toronto Market Week (Mode Show): save the date', 'Trade show invite'],
        ['Spring/Summer 2026 catalogues are now available', 'Catalogue launch']""")
rep("""      state: 'Screenshots coming',
""", """      approach: 'One system across sends: brand header, a short hero line, style blocks with style number, fabric and colour swatches, then showroom details and a catalogue download at the end.',
      gallery: [
        { src: I + 'dkr-email-essentials.webp', cap: 'F/W26 Essentials Collection' },
        { src: I + 'dkr-email-fleece.webp', cap: 'Ultra-soft brushed fleece' },
        { src: I + 'dkr-email-market-week.webp', cap: 'Toronto Market Week invite' }
      ],
""")
rep("""      const media = x.video""", """      const media = x.anim
        ? `<video src="${x.anim}" poster="${x.src}" width="${x.w}" height="${x.h}" muted loop playsinline preload="metadata" ${reduce ? 'controls' : 'autoplay'} aria-label="${attr(p.title + ': ' + x.cap)}"></video>`
        : x.video""")
open(p, 'w').write(s); print('patched')
