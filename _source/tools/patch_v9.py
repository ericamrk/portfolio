import os
p = os.path.join(os.path.dirname(__file__), '..', 'site', 'index.html'); s = open(p).read()
def rep(a, b):
    global s
    assert a in s, 'MISSING: ' + a[:80]; s = s.replace(a, b, 1)
rep('<dialog class="case" id="case" aria-labelledby="caseTitle">', '''<dialog class="viewer" id="viewer" aria-labelledby="viewerTitle">
  <div class="viewer-bar">
    <span class="mono" id="viewerTitle"></span>
    <div class="viewer-actions"><a class="mono" id="viewerOpen" href="#" target="_blank" rel="noopener">Open in new tab ↗</a><button class="case-close" type="button" id="viewerClose" aria-label="Close">✕</button></div>
  </div>
  <div class="viewer-body" id="viewerBody"></div>
</dialog>

<dialog class="case" id="case" aria-labelledby="caseTitle">''')
rep('/* ---------- Case study sheet ---------- */', '''/* ---------- File viewer (HTML pages, PDFs, full images) ---------- */
dialog.viewer { width: 100%; max-width: 100%; height: 100%; max-height: 100%; margin: 0; border: 0; padding: 0; background: var(--wall); color: var(--ink); }
dialog.viewer[open] { display: grid; grid-template-rows: auto minmax(0, 1fr); }
dialog.viewer::backdrop { background: rgba(20,20,18,.5); }
.viewer-bar { display: flex; justify-content: space-between; align-items: center; gap: 12px; background: var(--paper); border-bottom: 1px solid var(--line);
  padding: calc(env(safe-area-inset-top, 0px) + 10px) max(16px, env(safe-area-inset-right, 0px)) 10px max(16px, env(safe-area-inset-left, 0px)); }
.viewer-bar > span { min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--muted); }
.viewer-actions { display: flex; align-items: center; gap: 14px; flex: none; }
.viewer-actions a { color: var(--muted); }
.viewer-body { min-height: 0; overflow: auto; -webkit-overflow-scrolling: touch; }
.viewer-body iframe { display: block; width: 100%; height: 100%; border: 0; background: #fff; }
.viewer-body .pages { display: grid; justify-items: center; gap: 16px; padding: 20px max(16px, env(safe-area-inset-right, 0px)) calc(env(safe-area-inset-bottom, 0px) + 28px) max(16px, env(safe-area-inset-left, 0px)); }
.viewer-body .pages canvas, .viewer-body .pages img { display: block; max-width: min(100%, 1100px); height: auto; background: #fff; box-shadow: var(--shadow); }
.viewer-body .pages .pg { width: min(100%, 1100px); aspect-ratio: var(--ar, 8.5 / 11); background: var(--paper); display: grid; place-items: center; color: var(--muted); box-shadow: var(--shadow); }
.viewer-body .pages .pg canvas { width: 100%; max-width: 100%; }
.viewer-msg { padding: 40px 16px; text-align: center; color: var(--muted); }

/* ---------- Case study sheet ---------- */''')
rep("  /* ---------------- Case study sheet ---------------- */", r"""  /* ---------------- File viewer: links to our own files open here, not in a new tab ---------------- */
  const vdlg = $('#viewer'), vbody = $('#viewerBody');
  let pdfLib = null, pdfIO = null;
  const loadScript = src => new Promise((ok, no) => { const t = document.createElement('script'); t.src = src; t.onload = ok; t.onerror = no; document.head.append(t); });
  const getPdf = async () => {
    if (pdfLib) return pdfLib;
    const base = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/';
    await loadScript(base + 'pdf.min.js'); await loadScript(base + 'pdf.worker.min.js');
    return (pdfLib = window['pdfjs-dist/build/pdf']);
  };
  const openFile = async (href, title) => {
    const abs = new URL(href, location.href);
    $('#viewerTitle').textContent = title || decodeURIComponent(abs.pathname.split('/').pop());
    $('#viewerOpen').href = abs.href;
    vbody.innerHTML = '<p class="viewer-msg mono">Loading…</p>';
    pdfIO?.disconnect();
    if (!vdlg.open) vdlg.showModal();
    const ext = abs.pathname.split('.').pop().toLowerCase();
    try {
      if (ext === 'html') {
        let html = await (await fetch(abs)).text();
        const baseTag = `<base href="${new URL('./', abs).href}" target="_blank">`;
        html = /<head[^>]*>/i.test(html) ? html.replace(/<head[^>]*>/i, m => m + baseTag) : baseTag + html;
        const f = document.createElement('iframe'); f.title = title || 'Page'; f.srcdoc = html;
        vbody.innerHTML = ''; vbody.append(f);
      } else if (ext === 'pdf') {
        const lib = await getPdf();
        const doc = await lib.getDocument({ url: abs.href }).promise;
        const first = await doc.getPage(1), vp0 = first.getViewport({ scale: 1 });
        const wrap = document.createElement('div'); wrap.className = 'pages';
        wrap.style.setProperty('--ar', `${vp0.width} / ${vp0.height}`);
        for (let i = 1; i <= doc.numPages; i++) { const d = document.createElement('div'); d.className = 'pg mono'; d.dataset.n = i; d.textContent = `Page ${i}`; wrap.append(d); }
        vbody.innerHTML = ''; vbody.append(wrap);
        const draw = async el => {
          if (el.dataset.done) return; el.dataset.done = 1;
          const pg = await doc.getPage(+el.dataset.n), w = el.clientWidth || 900;
          const vp = pg.getViewport({ scale: (w / pg.getViewport({ scale: 1 }).width) * Math.min(devicePixelRatio || 1, 2) });
          const c = document.createElement('canvas'); c.width = vp.width; c.height = vp.height;
          c.setAttribute('role', 'img'); c.setAttribute('aria-label', `Page ${el.dataset.n} of ${doc.numPages}`);
          await pg.render({ canvasContext: c.getContext('2d'), viewport: vp }).promise;
          el.textContent = ''; el.append(c);
        };
        pdfIO = new IntersectionObserver(es => es.forEach(e => e.isIntersecting && draw(e.target)), { root: vbody, rootMargin: '600px 0px' });
        wrap.querySelectorAll('.pg').forEach(el => pdfIO.observe(el));
      } else {
        vbody.innerHTML = `<div class="pages"><img src="${abs.href}" alt="${attr(title || '')}"></div>`;
      }
    } catch (err) {
      vbody.innerHTML = `<p class="viewer-msg">This file could not be shown here. <a href="${abs.href}" target="_blank" rel="noopener">Open it in a new tab</a>.</p>`;
    }
  };
  $('#viewerClose').addEventListener('click', () => vdlg.close());
  vdlg.addEventListener('close', () => { pdfIO?.disconnect(); vbody.innerHTML = ''; });
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]'); if (!a || a.closest('#viewer')) return;
    const h = a.getAttribute('href');
    if (!/^(files|images)\//.test(h)) return;
    e.preventDefault();
    openFile(h, a.textContent.replace(/\s*↗\s*$/, '').trim());
  });

  /* ---------------- Case study sheet ---------------- */""")
open(p, 'w').write(s); print('patched')
