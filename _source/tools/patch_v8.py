import os, re
p = os.path.join(os.path.dirname(__file__), '..', 'site', 'index.html'); s = open(p).read()
def rep(a, b):
    global s
    assert a in s, 'MISSING: ' + a[:80]; s = s.replace(a, b, 1)
def cut(a_mark, b_mark, new):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a); s = s[:a] + new + s[b:]

# 1. hockey out
cut("    { id: 'gsw-hockey',", "\n    { id: ", "")
# 2. First Cover: keep as a draft, hidden until it is ready

rep("  const MENU = [", "  for (let i = PROJECTS.length - 1; i >= 0; i--) if (PROJECTS[i].draft) PROJECTS.splice(i, 1);\n  const MENU = [")
rep("  document.querySelectorAll('[data-count]').forEach(b => b.textContent = countOf(b.dataset.count));",
    "  document.querySelectorAll('[data-count]').forEach(b => { const n = countOf(b.dataset.count); b.textContent = n; if (!n) b.closest('button').hidden = true; });")
# 3. runway: video out; three FAT items back to Mass Exodus
rep("        { video: 'files/metamorphosis-runway.mp4', src: I + 'rw-mx-clip-poster.webp', cap: 'Runway clip' },\n", "")
for line in ["        { src: I + 'rw-bts-06.webp', cap: 'Looks lined up backstage' },\n",
             "        { src: I + 'rw-fit-01.webp', cap: 'Fitting in the studio' },\n"]:
    rep(line, "")
rep("        { src: I + 'rw-fit-02.webp', cap: 'Fitting in the studio' }", "")
s = re.sub(r"(\{ src: I \+ 'rw-bts-orb.webp', cap: 'Holding the orb' \}),\s*\n(\s*\] \},)", r"\1\n\2", s)
rep("        { src: I + 'rw-mx-05.webp', cap: 'Black cut-out dress' },",
    """        { src: I + 'rw-mx-05.webp', cap: 'Black cut-out dress' },
        { src: I + 'rw-bts-06.webp', cap: 'Looks lined up after the show' },
        { src: I + 'rw-fit-01.webp', cap: 'Before the show' },
        { src: I + 'rw-fit-02.webp', cap: 'Before the show' },""")
rep("{ sub: 'Backstage & fittings' }", "{ sub: 'Backstage' }")
# 4. Outcome block gone; empty blocks hidden instead of showing notes to self
rep("""      summary: 'Launch email for a new designer collection, with a lookbook guide to the season.',""",
    """      summary: 'Launch email for a new designer collection, with a lookbook guide to the season. Click-through rate rose 16% within 24 hours and order conversion 12%.',""")
cut("        <div><h4 class=\"mono\">Outcome</h4>", "        <div><h4 class=\"mono\">${p.a11y", "")
rep("""        <div><h4 class="mono">Approach</h4>${p.approach ? `<p>${p.approach}</p>` : todo('Concept, layout decisions, how it adapts across sizes or channels.')}</div>""",
    """        ${p.approach ? `<div><h4 class="mono">Approach</h4><p>${p.approach}</p></div>` : ''}""")
a = s.index("        <div><h4 class=\"mono\">${p.a11y"); b = s.index("\n", a)
s = s[:a] + """        ${p.a11yText ? `<div><h4 class="mono">${p.a11y ? 'Accessibility' : 'Production'}</h4><p>${p.a11yText}</p></div>` : ''}""" + s[b:]
rep("""        <div><span class="mono">Role</span>${p.role ? `<span>${p.role}</span>` : '<span class="todo">To add</span>'}</div>""",
    """        ${p.role ? `<div><span class="mono">Role</span><span>${p.role}</span></div>` : ''}""")
# 5. window section
rep("""        { src: I + 'wdlt-window-mockup.webp', cap: 'Window design, mock-up' },
        { src: I + 'wdlt-sandwich.webp', cap: 'Sandwich board on the street' },""",
    """        { src: I + 'wdlt-window-mockup.webp', cap: 'Wanderlust window, design mock-up' },
        { src: I + 'wdlt-window-installed.webp', cap: 'Wanderlust window, installed' },
        { src: I + 'wdlt-window-street.webp', cap: 'The window from the street' },
        { src: I + 'wdlt-sandwich.webp', cap: 'Sandwich board on the street' },""")
open(p, 'w').write(s); print('patched')
