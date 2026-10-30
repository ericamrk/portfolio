import os
p = os.path.join(os.path.dirname(__file__), '..', 'site', 'index.html'); s = open(p).read()
def rep(a, b):
    global s
    assert a in s, 'MISSING: ' + a[:80]; s = s.replace(a, b, 1)
def cut(a_mark, b_mark, new, inclusive=False):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a)
    if inclusive: b += len(b_mark)
    s = s[:a] + new + s[b:]

# ---------- contact: phone out, Instagram in ----------
rep("""          <p class="mono" style="color:var(--muted);margin:14px 0 0">647-618-5601 · Toronto, ON</p>""",
    """          <p class="mono" style="color:var(--muted);margin:14px 0 0">Instagram <a href="https://www.instagram.com/erica_rk/" target="_blank" rel="noopener">@erica_rk</a> · Toronto, ON</p>""")

# ---------- captions ----------
rep("""        { src: I + 'wdlt-o-them.webp', cap: 'Ô, Them' },\n""", "")
rep("""        { src: I + 'wdlt-nea-us.webp', cap: 'Neandertal, Us' },""",
    """        { src: I + 'wdlt-nea-us.webp', cap: 'Neandertal, Us' },
        { src: I + 'wdlt-o-them.webp', cap: 'Neandertal, Them' },""")
rep("{ head: 'Social media · fragrance' }", "{ head: 'Social media · fragrance', note: 'Neandertal and Ô' }")

# ---------- emails: one folder per email, half-length preview ----------
rep("""        { src: I + 'dkr-email-essentials.webp', cap: 'F/W26 Essentials Collection' },
        { src: I + 'dkr-email-fleece.webp', cap: 'Ultra-soft brushed fleece' },
        { src: I + 'dkr-email-market-week.webp', cap: 'Toronto Market Week invite' }""",
"""        { head: 'FW26 Essentials', note: 'Collection launch' },
        { mail: I + 'dkr-email-essentials.webp', src: I + 'dkr-email-essentials-half.webp', cap: 'The F/W26 Essentials Collection, now in stock' },
        { head: 'FW26 Fleece', note: 'Restock' },
        { mail: I + 'dkr-email-fleece.webp', src: I + 'dkr-email-fleece-half.webp', cap: 'Ultra-soft brushed fleece, now in stock' },
        { head: 'FW26 Market Week', note: 'Trade show invite' },
        { mail: I + 'dkr-email-market-week.webp', src: I + 'dkr-email-market-week-half.webp', cap: 'Toronto Market Week (Mode Show), save the date' }""")
rep("""        { label: 'SS26 catalogues · email A',""", """        { label: 'Live email · SS26 catalogues A',""")
rep("""        { label: 'SS26 catalogues · email B',""", """        { label: 'Live email · SS26 catalogues B',""")
rep("""        { label: 'The Casual Elegance Collection',""", """        { label: 'Live email · Casual Elegance',""")

# ---------- runway: two folders, backstage inside Fashion Art Toronto ----------
rep("""        { head: 'Backstage & fittings' },""", """        { sub: 'Backstage & fittings' },""")

# ---------- renderer: folders ----------
cut("  const stackHTML = p => {", "\n  };\n", r"""  const layout = list => {
    const items = list.map(x => {
      if (x.sub) return { ...x, kind: 'sub' };
      const [w, h] = DIMS[x.src] || [4, 5];
      return { ...x, w, h, kind: x.mail ? 'mail' : w / h > 1.15 ? 'span' : 'half' };
    });
    for (let i = 0; i < items.length;) {
      if (items[i].kind !== 'half') { i++; continue; }
      let j = i; while (j < items.length && items[j].kind === 'half') j++;
      if ((j - i) % 2) items[j - 1].kind = 'solo';
      i = j;
    }
    return items;
  };
  const figHTML = (p, x, n, eager) => {
    const label = attr(p.title + ': ' + x.cap);
    if (x.kind === 'sub') return `<div class="head"><h4>${x.sub}</h4></div>`;
    if (x.kind === 'mail') return `<figure class="mail">
        <div class="mail-prev"><img src="${x.src}" alt="${label}, first half" width="${x.w}" height="${x.h}"${eager ? '' : ' loading="lazy"'} decoding="async"></div>
        <figcaption><span class="mono">${x.cap}</span><a class="btn" href="${x.mail}" target="_blank" rel="noopener">View the full email ↗</a></figcaption>
      </figure>`;
    const media = x.anim
      ? `<video src="${x.anim}" poster="${x.src}" width="${x.w}" height="${x.h}" muted loop playsinline preload="metadata" ${reduce ? 'controls' : 'autoplay'} aria-label="${label}"></video>`
      : x.video
      ? `<video src="${x.video}" poster="${x.src}" width="${x.w}" height="${x.h}" controls muted playsinline loop preload="none" aria-label="${label}"></video>`
      : `<img src="${x.src}" alt="${label}" width="${x.w}" height="${x.h}"${eager ? '' : ' loading="lazy"'} decoding="async">`;
    return `<figure class="${x.kind}">${media}<figcaption class="mono">${pad2(n)} · ${x.cap}</figcaption></figure>`;
  };
  const stackHTML = p => {
    const g = p.gallery || [];
    if (!g.length) return `<div class="ph case-hero">${p.state || 'Images coming'}</div>`;
    if (!g.some(x => x.head)) {
      let n = 0;
      return `<div class="stack">${layout(g).map((x, i) => figHTML(p, x, x.kind === 'sub' ? n : ++n, i < 3)).join('')}</div>`;
    }
    const secs = [];
    g.forEach(x => { if (x.head) secs.push({ head: x.head, note: x.note, items: [] }); else secs[secs.length - 1]?.items.push(x); });
    const tabs = secs.map((sec, k) => `<button type="button" role="tab" id="ft-${p.id}-${k}" aria-controls="fp-${p.id}-${k}" aria-selected="${k === 0}" tabindex="${k === 0 ? 0 : -1}" class="ftab f${k % 4}">
        <span class="mono">${pad2(k + 1)}</span>${sec.head}</button>`).join('');
    const panels = secs.map((sec, k) => {
      let n = 0;
      const count = sec.items.filter(x => !x.sub).length;
      return `<div role="tabpanel" id="fp-${p.id}-${k}" aria-labelledby="ft-${p.id}-${k}" class="fpanel f${k % 4}"${k ? ' hidden' : ''}>
        <div class="fpanel-top mono"><span>${sec.note || sec.head}</span><span>${count} ${count === 1 ? 'piece' : 'pieces'}</span></div>
        <div class="stack">${layout(sec.items).map((x, i) => figHTML(p, x, x.kind === 'sub' ? n : ++n, k === 0 && i < 3)).join('')}</div>
      </div>`;
    }).join('');
    return `<section class="folders" aria-label="${attr(p.title)} sections"><div class="ftabs" role="tablist">${tabs}</div>${panels}</section>`;
  };
  const selectFolder = (tab, focus) => {
    const root = tab.closest('.folders');
    root.querySelectorAll('[role=tab]').forEach(t => {
      const on = t === tab;
      t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
      root.querySelector('#' + t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
    const top = root.getBoundingClientRect().top, box = $('#caseIn').getBoundingClientRect().top;
    if (top < box) root.scrollIntoView({ block: 'start', behavior: reduce ? 'auto' : 'smooth' });
  };
  $('#caseIn').addEventListener('click', e => { const t = e.target.closest('.ftab'); if (t) selectFolder(t); });
  $('#caseIn').addEventListener('keydown', e => {
    const t = e.target.closest('.ftab'); if (!t || !['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(e.key)) return;
    const all = [...t.parentNode.children], i = all.indexOf(t);
    const n = e.key === 'Home' ? 0 : e.key === 'End' ? all.length - 1 : (i + (e.key === 'ArrowRight' ? 1 : -1) + all.length) % all.length;
    e.preventDefault(); selectFolder(all[n], true);
  });""", inclusive=False)

# ---------- CSS ----------
rep(""".stack video { display: block; width: 100%; height: auto; background: #000; }""", """.stack video { display: block; width: 100%; height: auto; background: #000; }

/* ---------- Folders (sections inside a project) ---------- */
.folders { display: grid; padding-top: 6px; }
.ftabs { display: flex; align-items: flex-end; overflow-x: auto; scrollbar-width: none; padding: 0 0 0 6px; margin-bottom: -1px; }
.ftabs::-webkit-scrollbar { display: none; }
.ftab {
  flex: none; position: relative; display: flex; align-items: baseline; gap: 10px; margin-left: -10px;
  padding: 11px 22px 12px 18px; border: 0; border-radius: 12px 12px 0 0; cursor: pointer;
  font: 400 13px/1 var(--f-mono); letter-spacing: .02em; color: var(--ink); background: var(--fc);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35), 0 -2px 6px rgba(20,20,18,.05);
  transform: translateY(6px); transition: transform .25s cubic-bezier(.22,1,.36,1);
}
.ftab:first-child { margin-left: 0; }
.ftab .mono { font-size: 10px; color: inherit; opacity: .6; }
.ftab:hover { transform: translateY(2px); }
.ftab[aria-selected="true"] { transform: none; z-index: 2; padding-bottom: 16px; }
.f0 { --fc: var(--folder-0); } .f1 { --fc: var(--folder-1); } .f2 { --fc: var(--folder-2); } .f3 { --fc: var(--folder-3); }
.fpanel { position: relative; z-index: 1; background: var(--fc); padding: clamp(14px, 2.4vw, 24px); border-radius: 0 12px 12px 12px; }
.fpanel-top { display: flex; justify-content: space-between; gap: 12px; color: var(--ink); opacity: .7; margin-bottom: 14px; }
.fpanel .stack { padding-top: 0; }
.fpanel .stack figcaption { color: var(--ink); opacity: .72; }
.fpanel .stack .head { border-color: color-mix(in srgb, var(--ink) 18%, transparent); }
.stack .mail { grid-column: 1 / -1; width: min(100%, 520px); justify-self: center; gap: 12px; }
.mail-prev { position: relative; max-width: 100%; overflow: hidden; background: var(--paper); box-shadow: var(--shadow); }
.mail-prev::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 38%; background: linear-gradient(to bottom, transparent, var(--fc, var(--paper)) 92%); pointer-events: none; }
.stack .mail figcaption { display: grid; justify-items: center; gap: 12px; text-align: center; margin-top: -48px; position: relative; z-index: 1; }""")
rep("""  --shadow: 0 1px 2px rgba(20,20,18,.08), 0 8px 24px rgba(20,20,18,.07);""", """  --shadow: 0 1px 2px rgba(20,20,18,.08), 0 8px 24px rgba(20,20,18,.07);
  --folder-0: #d6dde2; --folder-1: #c9b8a6; --folder-2: #a9bfd0; --folder-3: #dcd6c7;""")
s = s.replace("""    --oxide: #d9825f; --hatch: #262624; --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);""",
              """    --oxide: #d9825f; --hatch: #262624; --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
    --folder-0: #2c3237; --folder-1: #3a332c; --folder-2: #2b3742; --folder-3: #34322b;""")
s = s.replace("""  --oxide: #d9825f; --hatch: #262624; --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
  color-scheme: dark;""", """  --oxide: #d9825f; --hatch: #262624; --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
  --folder-0: #2c3237; --folder-1: #3a332c; --folder-2: #2b3742; --folder-3: #34322b;
  color-scheme: dark;""")
open(p, 'w').write(s); print('patched', s.count('--folder-0'))
