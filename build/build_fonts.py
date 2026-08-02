import base64, io, os
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

SCRATCH = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(SCRATCH, 'portfolio.html'), encoding='utf-8').read()

chars = set(html)
chars.update(chr(c) for c in range(0x20, 0x7F))
chars.update('，。！？：；、「」『』（）—⋯・｜％＋')
text = ''.join(chars)

font = TTFont(os.path.join(SCRATCH, 'NotoSansTC.ttf'))
font = instancer.instantiateVariableFont(font, {'wght': 700})

opts = Options()
opts.flavor = 'woff2'
opts.desubroutinize = True
ss = Subsetter(options=opts)
ss.populate(text=text)
ss.subset(font)
buf = io.BytesIO()
font.save(buf)
data = base64.b64encode(buf.getvalue()).decode()
print(f'NotoTC 700 subset: {len(buf.getvalue())/1024:.0f} KB')

css = ("@font-face{font-family:'NotoTC';font-weight:700;font-display:swap;"
       "src:url(data:font/woff2;base64,%s) format('woff2')}" % data)
open(os.path.join(SCRATCH, 'fonts.css'), 'w', encoding='utf-8').write(css)
print('fonts.css written')
