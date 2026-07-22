import pathlib
from playwright.sync_api import sync_playwright
BASE=pathlib.Path(__file__).parent
LOGO="data:image/png;base64,"+pathlib.Path("/tmp/logo_b64.txt").read_text().strip()
HTML=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1200px;height:630px;overflow:hidden}}
body{{background:#0a0e13;color:#e8edf2;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,sans-serif}}
.bg{{position:absolute;inset:0}}
.bg::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 60% at 20% 40%,rgba(0,201,122,.16) 0%,transparent 60%),radial-gradient(ellipse 50% 50% at 92% 95%,rgba(255,90,90,.10) 0%,transparent 60%)}}
.bg::after{{content:'';position:absolute;inset:0;opacity:.5;background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:44px 44px}}
.edge{{position:absolute;left:0;top:0;bottom:0;width:8px;background:linear-gradient(#00c97a,#0a8f57)}}
.wrap{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 90px}}
.top{{display:flex;align-items:center;gap:14px;margin-bottom:30px}}
.top img{{width:54px;height:54px;object-fit:contain}}
.top span{{font-size:19px;font-weight:700;letter-spacing:3px;color:#9fb0bd;text-transform:uppercase}}
.top .k{{color:#00c97a}}
h1{{font-size:70px;font-weight:800;letter-spacing:-1.5px;line-height:1.04;color:#fff;max-width:1000px}}
.sub{{font-size:32px;font-weight:600;color:#00c97a;margin-top:20px}}
.chips{{display:flex;gap:12px;margin-top:34px}}
.chip{{font-size:19px;font-weight:600;color:#9fb0bd;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);padding:8px 18px;border-radius:40px}}
.url{{position:absolute;right:90px;bottom:52px;font-size:21px;color:#5b6b78;font-weight:600}}
</style></head><body>
<div class="bg"></div><div class="edge"></div>
<div class="wrap">
  <div class="top"><img src="{LOGO}"><span>Defence Intelligence <span class="k">· Analyse</span></span></div>
  <h1>La faille Hugging Face</h1>
  <div class="sub">Quand une IA autonome orchestre l'attaque</div>
  <div class="chips"><span class="chip">IA offensive</span><span class="chip">Supply chain IA</span><span class="chip">Juillet 2026</span></div>
</div>
<div class="url">defintelligence.fr/blog</div>
</body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1200,"height":630},device_scale_factor=1)
    pg.set_content(HTML); pg.screenshot(path=str(BASE/"assets/img/og-hugging-face.png")); print("ok"); b.close()
