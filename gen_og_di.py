#!/usr/bin/env python3.11
"""Génère les cartes de partage 1200x630 pour defintelligence.fr (Playwright)."""
import pathlib
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(__file__).parent
LOGO = "data:image/png;base64," + pathlib.Path("/tmp/logo_b64.txt").read_text().strip()

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden}
body{background:#0a0e13;color:#e8edf2;position:relative;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,sans-serif}
.bg{position:absolute;inset:0}
.bg::before{content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse 60% 60% at 22% 45%, rgba(0,201,122,.16) 0%, transparent 60%),
             radial-gradient(ellipse 50% 50% at 90% 90%, rgba(0,201,122,.08) 0%, transparent 60%)}
.bg::after{content:'';position:absolute;inset:0;opacity:.5;
  background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);
  background-size:44px 44px}
.edge{position:absolute;left:0;top:0;bottom:0;width:8px;background:linear-gradient(#00c97a,#0a8f57)}
.wrap{position:absolute;inset:0;display:flex;align-items:center;gap:56px;padding:0 90px}
.logo{width:300px;height:300px;flex-shrink:0;object-fit:contain;
  filter:drop-shadow(0 0 40px rgba(0,201,122,.35))}
.brand .kicker{font-size:20px;font-weight:700;letter-spacing:5px;color:#00c97a;text-transform:uppercase}
.brand h1{font-size:76px;font-weight:800;letter-spacing:-1.5px;line-height:1.02;margin:14px 0 20px;color:#fff}
.brand .tag{font-size:30px;font-weight:600;color:#9fb0bd;line-height:1.4}
.brand .tag b{color:#00c97a;font-weight:700}
.url{position:absolute;right:90px;bottom:54px;font-size:22px;color:#5b6b78;font-weight:600;letter-spacing:.5px}
"""

DEFAULT = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="bg"></div><div class="edge"></div>
<div class="wrap">
  <img class="logo" src="{LOGO}">
  <div class="brand">
    <div class="kicker">Cybersécurité · Renseignement</div>
    <h1>Defence<br>Intelligence</h1>
    <div class="tag"><b>Audit de sécurité</b> · <b>ASM</b> · <b>Threat Intelligence</b><br>Conseil indépendant · PME &amp; ETI · France</div>
  </div>
</div>
<div class="url">defintelligence.fr</div>
</body></html>"""

CTI = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}
.cti .wrap{{flex-direction:column;align-items:flex-start;justify-content:center;gap:0}}
.cti .top{{display:flex;align-items:center;gap:16px;margin-bottom:34px}}
.cti .top img{{width:60px;height:60px;object-fit:contain}}
.cti .top span{{font-size:22px;font-weight:700;letter-spacing:3px;color:#9fb0bd;text-transform:uppercase}}
.cti h1{{font-size:96px;font-weight:800;letter-spacing:-2px;line-height:.98;color:#fff}}
.cti h1 em{{color:#00c97a;font-style:normal}}
.cti .sub{{font-size:34px;font-weight:600;color:#9fb0bd;margin-top:22px}}
.cti .chips{{display:flex;gap:12px;margin-top:30px}}
.cti .chip{{font-size:20px;font-weight:600;color:#00c97a;border:1px solid rgba(0,201,122,.35);
  background:rgba(0,201,122,.08);padding:9px 20px;border-radius:40px}}
</style></head><body class="cti">
<div class="bg"></div><div class="edge"></div>
<div class="wrap">
  <div class="top"><img src="{LOGO}"><span>Defence Intelligence</span></div>
  <h1>CTI <em>Digest</em></h1>
  <div class="sub">Veille cybersécurité quotidienne</div>
  <div class="chips"><span class="chip">CVE critiques</span><span class="chip">Ransomware</span><span class="chip">Campagnes</span><span class="chip">Menaces</span></div>
</div>
<div class="url">defintelligence.fr/cti</div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1200,"height":630}, device_scale_factor=1)
    pg.set_content(DEFAULT); pg.screenshot(path=str(BASE/"static/img/og.png")); print("✓ og.png")
    pg.set_content(CTI); pg.screenshot(path=str(BASE/"static/img/og-cti.png")); print("✓ og-cti.png")
    b.close()
