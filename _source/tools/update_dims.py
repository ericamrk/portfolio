"""Write the pixel size of every image in site/images into index.html (between /*DIMS*/ and /*END*/)."""
import json, os, re
from PIL import Image
SITE = os.path.join(os.path.dirname(__file__), '..', 'site')
dims = {}
import re as _re
_old = _re.search(r'/\*DIMS\*/(.*?)/\*END\*/', open(os.path.join(SITE, 'index.html')).read(), _re.S)
if _old: dims.update(json.loads(_old.group(1)))
for f in sorted(os.listdir(os.path.join(SITE, 'images'))):
    with Image.open(os.path.join(SITE, 'images', f)) as im:
        dims['images/' + f] = list(im.size)
p = os.path.join(SITE, 'index.html'); s = open(p).read()
blob = '/*DIMS*/' + json.dumps(dims, separators=(',', ':')) + '/*END*/'
s = re.sub(r'/\*DIMS\*/.*?/\*END\*/', lambda m: blob, s, flags=re.S) if '/*DIMS*/' in s else s.replace("  const I = 'images/';", "  const DIMS = " + blob + ";\n  const I = 'images/';", 1)
open(p, 'w').write(s); print(len(dims), 'images')
