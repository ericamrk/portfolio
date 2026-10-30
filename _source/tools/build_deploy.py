"""Build a standalone website from site/ into deploy/ (+ zip) for Vercel / any static host."""
import os, shutil, re, zipfile
ROOT = os.path.join(os.path.dirname(__file__), '..'); SITE = os.path.join(ROOT, 'site'); OUT = os.path.join(ROOT, 'deploy', 'rongke-ma-portfolio')
SKIP = {'files/metamorphosis-runway.mp4', 'images/rw-mx-clip-poster.webp', 'images/old-rombaut.webp'}
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
for d in ['images', 'files']:
    for dp, _, fs in os.walk(os.path.join(SITE, d)):
        for f in fs:
            rel = os.path.relpath(os.path.join(dp, f), SITE)
            if rel in SKIP or f.startswith('.'): continue
            os.makedirs(os.path.join(OUT, os.path.dirname(rel)), exist_ok=True)
            shutil.copy2(os.path.join(dp, f), os.path.join(OUT, rel))
body = open(os.path.join(SITE, 'index.html')).read()
body = re.sub(r'^<meta charset="utf-8">\n', '', body)
head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Rongke (Erica) Ma, graphic designer in Toronto: campaigns, HTML email, landing pages, print and motion for fashion and lifestyle brands.">
<meta property="og:title" content="Rongke (Erica) Ma · Graphic Designer">
<meta property="og:description" content="Campaigns, HTML email, landing pages, print and motion. Toronto.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23151514'/%3E%3Ctext x='16' y='22' font-family='Arial' font-size='15' fill='%23fafaf7' text-anchor='middle'%3ERM%3C/text%3E%3C/svg%3E">
<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
open(os.path.join(OUT, 'index.html'), 'w').write(head + body + '\n</body>\n</html>\n')
z = os.path.join(ROOT, 'deploy', 'rongke-ma-portfolio.zip')
if os.path.exists(z): os.remove(z)
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
    for dp, _, fs in os.walk(OUT):
        for f in fs:
            full = os.path.join(dp, f); zf.write(full, os.path.relpath(full, os.path.dirname(OUT)))
n = sum(len(fs) for _, _, fs in os.walk(OUT)); print(n, 'files', os.path.getsize(z) // 1024, 'KB zip')
