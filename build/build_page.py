import base64, os
BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
def read(name, base=BUILD):
    return open(os.path.join(base, name), encoding='utf-8').read()
html = read('portfolio.html', ROOT)
html = html.replace('/*FONTS*/', read('fonts.css'))
html = html.replace('/*THUMBS*/', read('thumbs.css'))
photo = base64.b64encode(open(os.path.join(BUILD, 'photo.jpg'), 'rb').read()).decode()
html = html.replace('__PHOTO__', photo)
html = html.replace('__CLAUDE__', read('claude.path'))
# Artifact version: raw fragment (claude.ai wraps it itself)
out = os.path.join(ROOT, 'portfolio_final.html')
open(out, 'w', encoding='utf-8').write(html)

# Web version (GitHub Pages): full standalone document
import re
m = re.search(r'<title>(.*?)</title>', html)
title = m.group(1) if m else 'Cinzz Studio'
body = html.replace(m.group(0), '', 1) if m else html
web = (
    '<!doctype html>\n<html lang="zh-Hant">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    f'<title>{title}</title>\n'
    '<meta name="description" content="Cinzia — 影片剪輯師與視覺設計師。專注 YouTube 長影音、知識型內容與個人品牌影片。">\n'
    '</head>\n<body>\n' + body + '\n</body>\n</html>\n'
)
out2 = os.path.join(ROOT, 'index.html')
open(out2, 'w', encoding='utf-8').write(web)
print('portfolio_final.html', os.path.getsize(out) // 1024, 'KB /', 'index.html', os.path.getsize(out2) // 1024, 'KB')
