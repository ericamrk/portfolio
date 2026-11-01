import os
p = os.path.join(os.path.dirname(__file__), '..', 'site', 'index.html'); s = open(p).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, 'NOT UNIQUE/MISSING: ' + a[:80]; s = s.replace(a, b, 1)
def cut(a_mark, b_mark, new):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a); s = s[:a] + new + s[b:]

# ---------- Metamorphosis collection: five look folders ----------
cut("    { id: 'metamorphosis',", "    { id: 'runway',", r"""    { id: 'metamorphosis', title: 'Metamorphosis', client: 'TMU thesis · Fashion Art Toronto', year: '2024',
      cover: I + 'meta-l1-orb.webp',
      summary: 'A five-look thesis collection about rebirth and transformation, each look a stage in a creature\'s life. Selected by Fashion Art Toronto for an additional showcase.',
      cats: ['collection'], role: 'Designer and creative director', deliverables: 'Five-look collection, editorial shoot and campaign images', tools: '3D printing and electroplating, hand-dyeing, pattern making, Photoshop',
      brief: 'The Metamorphosis collection explores the journey of rebirth and transformation, with each look reflecting a stage in a unique creature\'s life, mirroring human experiences of growth, change and self-discovery.',
      approach: 'Photography @teerunner · Makeup @zohairkeswani · Hair @mxz_hmua · Design and creative direction @erica_rk',
      gallery: [
        { head: 'Look 1 · Incubation', note: 'Silver liquid satin, 3D-printed shell' },
        { src: I + 'meta-l1-orb.webp', cap: 'The electroplated shell' },
        { src: I + 'meta-l1-front.webp', cap: 'Front' },
        { src: I + 'meta-l1-side.webp', cap: 'Side' },
        { text: '"Incubation" symbolizes a sacred beginning. Silver liquid satin embodies the blank canvas of life, while a 3D-printed, electroplated shell adds a futuristic element. The look shows the fragility and strength of the newborn.', credit: 'Model @brandypaul_' },
        { head: 'Look 2 · Emergence Evolution', note: '3D-printed structures, hand-dyed fabric' },
        { src: I + 'meta-l2-full.webp', cap: 'Full look' },
        { src: I + 'meta-l2-portrait.webp', cap: 'Portrait' },
        { src: I + 'meta-l2-side.webp', cap: 'Side' },
        { text: '"Emergence Evolution" embodies the next step in the journey: growth. Combining 3D-printed structures with hand-dyed fabric, this look represents the stage where life begins to unfold and take shape, a time of strength, discovery and newfound potential.', credit: 'Model @muchenn___' },
        { head: 'Look 3 · Awakening', note: 'PU leather cape, rooster-feather bodysuit' },
        { src: I + 'meta-l3-front.webp', cap: 'Front, cape open' },
        { src: I + 'meta-l3-cape.webp', cap: 'The cape, side' },
        { src: I + 'meta-l3-feathers.webp', cap: 'Feather bodysuit through the cape' },
        { src: I + 'meta-l3-profile.webp', cap: 'Profile' },
        { text: '"Awakening" symbolizes the breakthrough from confusion to clarity. A PU leather cape paired with a rooster-feather bodysuit evokes the feeling of breaking free from a shell: the moment of awakening and self-realization in the life journey.', credit: 'Model @stupid.intellectual' },
        { head: 'Look 4 · Ascension', note: 'Feathered half-skirt' },
        { src: I + 'meta-l4-back.webp', cap: 'Back' },
        { src: I + 'meta-l4-side.webp', cap: 'Side' },
        { src: I + 'meta-l4-front.webp', cap: 'Front' },
        { text: '"Ascension" represents the peak of transformation and rebirth and is the highlight of the collection. The feathered half-skirt symbolizes a magnificent metamorphosis, reflecting the most radiant moments in life, when one truly shines at their brightest.', credit: 'Model @mmalhvx' },
        { head: 'Look 5 · Eternity in a Moment', note: 'Bird-skull top, torn tulle with rhinestones' },
        { src: I + 'meta-l5-dress.webp', cap: 'Front' },
        { src: I + 'meta-l5-hands.webp', cap: 'The bodice' },
        { src: I + 'meta-l5-back.webp', cap: 'Back' },
        { src: I + 'meta-l5-portrait.webp', cap: 'Portrait' },
        { text: '"Eternity in a Moment" represents the final stage of life. The top draws on the shape of a bird\'s skull, while the skirt, adorned with rhinestones on torn, delicate tulle, glimmers with the beauty of life\'s closing moments. Looking back, each stage of life brings us closer to completeness. Death is not an end but a natural, profound transition, part of life\'s endless cycle, inviting reflection on the beauty of all we have become.', credit: 'Model @rhea.kathleenn' }
      ] },

""")

# ---------- renderer: text block at the end of a folder ----------
rep("      if (x.sub) return { ...x, kind: 'sub' };", "      if (x.sub) return { ...x, kind: 'sub' };\n      if (x.text) return { ...x, kind: 'text' };")
rep("    if (x.kind === 'sub') return `<div class=\"head\"><h4>${x.sub}</h4></div>`;",
    "    if (x.kind === 'sub') return `<div class=\"head\"><h4>${x.sub}</h4></div>`;\n    if (x.kind === 'text') return `<div class=\"look-note\"><p>${x.text}</p>${x.credit ? `<span class=\"mono\">${x.credit}</span>` : ''}</div>`;")
s = s.replace("figHTML(p, x, x.kind === 'sub' ? n : ++n,", "figHTML(p, x, (x.kind === 'sub' || x.kind === 'text') ? n : ++n,")
rep("      const count = sec.items.filter(x => !x.sub).length;", "      const count = sec.items.filter(x => !x.sub && !x.text).length;")
rep(".stack video { display: block;", """.stack .look-note { grid-column: 1 / -1; display: grid; gap: 10px; max-width: 62ch; padding-top: 14px; border-top: 1px solid color-mix(in srgb, var(--ink) 18%, transparent); }
.stack .look-note p { margin: 0; font: 300 clamp(17px, 1.7vw, 20px)/1.5 var(--f-display); font-stretch: 108%; color: var(--ink); }
.stack .look-note .mono { color: var(--ink); opacity: .65; }
.stack video { display: block;""")
# the approach block is credits here: label it Credits
rep("""        ${p.approach ? `<div><h4 class="mono">Approach</h4><p>${p.approach}</p></div>` : ''}""",
    """        ${p.approach ? `<div><h4 class="mono">${p.id === 'metamorphosis' ? 'Credits' : 'Approach'}</h4><p>${p.approach}</p></div>` : ''}""")

# ---------- runway: drop the duplicate (FAT 08), new cover (FAT 06) ----------
rep("        { src: I + 'rw-fat-07.webp', cap: 'White cape, back view' },\n", "")
rep("      cover: I + 'rw-fat-01.webp',", "      cover: I + 'rw-fat-05.webp',")
# ---------- editorial cover = its 05; Light rain cover = its 01 ----------
rep("      cover: I + 'meta-ed-projection.webp',", "      cover: I + 'meta-ed-glow-forest.webp',")
rep("      cover: I + 'uniqlo-ad-cover.webp',", "      cover: I + 'uniqlo-ad-landscape.webp',")
open(p, 'w').write(s); print('patched')
