#!/usr/bin/env python3
"""GitHub Repositories PDF Report Generator - Ephemeral Script"""
from datetime import datetime
from jinja2 import Template
from weasyprint import HTML

# Data
USER = {"name": "Gloria Peralta", "login": "gloriaperaltav"}
REPOS = [
    {"name": "qa_cypress_orion", "lang": "TypeScript", "stars": 0, "updated": "12 Mar 2025", "url": "https://github.com/gloriaperaltav/qa_cypress_orion"},
    {"name": "TEST", "lang": "—", "stars": 0, "updated": "4 Sep 2026", "url": "https://github.com/gloriaperaltav/TEST"}
]
STATS = {"public": 2, "private": 0, "size": "3.7 KB"}

HTML_TPL = """<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Informe GitHub</title><style>
@page{size:A4;margin:2cm}*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',sans-serif;color:#24292e;line-height:1.6}
.header{border-bottom:3px solid #0366d6;padding-bottom:20px;margin-bottom:30px}
.header h1{color:#0366d6;font-size:28px;margin-bottom:5px}
.header p{color:#586069;font-size:13px}
.user-info{background:#f6f8fa;border-left:4px solid #0366d6;padding:15px;margin-bottom:30px;border-radius:3px}
.user-info h2{color:#0366d6;font-size:15px;margin-bottom:8px}
.user-info p{font-size:12px;color:#586069;margin:4px 0}
.stats-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-bottom:30px}
.stat-card{background:#f6f8fa;border:1px solid #e1e4e8;padding:15px;border-radius:6px;text-align:center}
.stat-card .num{font-size:24px;font-weight:bold;color:#0366d6;margin-bottom:5px}
.stat-card .lbl{font-size:11px;color:#586069;text-transform:uppercase;letter-spacing:0.5px}
.section{color:#0366d6;font-size:18px;font-weight:600;margin-top:30px;margin-bottom:15px;border-bottom:2px solid #e1e4e8;padding-bottom:10px}
table{width:100%;border-collapse:collapse;margin-bottom:20px;font-size:12px}
thead{background:#f6f8fa;border-bottom:2px solid #0366d6}
th{padding:12px;text-align:left;font-weight:600;color:#0366d6}
td{padding:12px;border-bottom:1px solid #e1e4e8}
tbody tr:hover{background:#f6f8fa}
.repo{background:#f6f8fa;border:1px solid #e1e4e8;border-radius:6px;padding:15px;margin-bottom:15px}
.repo h3{color:#0366d6;font-size:14px;margin-bottom:8px}
.repo .meta{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;font-size:11px;color:#586069}
.repo .meta strong{color:#24292e;margin-right:5px}
.badge{display:inline-block;padding:3px 8px;background:#d4edda;color:#155724;border-radius:12px;font-size:10px;font-weight:500}
.footer{margin-top:40px;padding-top:15px;border-top:1px solid #e1e4e8;text-align:center;font-size:10px;color:#6a737d}
</style></head><body>
<div class="header"><h1>📊 Informe de Repositorios GitHub</h1><p>{{ date }} | {{ user_name }} (@{{ user_login }})</p></div>
<div class="user-info"><h2>👤 Usuario</h2><p><strong>Nombre:</strong> {{ user_name }}</p><p><strong>Login:</strong> @{{ user_login }}</p></div>
<div class="stats-grid">
<div class="stat-card"><div class="num">{{ public }}</div><div class="lbl">Públicos</div></div>
<div class="stat-card"><div class="num">{{ private }}</div><div class="lbl">Privados</div></div>
<div class="stat-card"><div class="num">{{ size }}</div><div class="lbl">Tamaño Total</div></div>
</div>
<h2 class="section">📦 Resumen</h2>
<table><thead><tr><th>Nombre</th><th>Lenguaje</th><th>⭐</th><th>Actualizado</th></tr></thead><tbody>
{% for r in repos %}<tr><td><strong>{{ r.name }}</strong></td><td>{{ r.lang }}</td><td>{{ r.stars }}</td><td>{{ r.updated }}</td></tr>{% endfor %}
</tbody></table>
<h2 class="section">🔍 Detalles</h2>
{% for r in repos %}<div class="repo"><h3>{{ r.name }}</h3><div class="meta">
<div><strong>Lenguaje:</strong> {{ r.lang }}</div><div><strong>Estrellas:</strong> {{ r.stars }}</div>
<div><strong>Actualizado:</strong> {{ r.updated }}</div><div><strong>URL:</strong> <a href="{{ r.url }}">GitHub</a></div>
</div></div>{% endfor %}
<div class="footer"><p>Generado automáticamente | GitHub Report Generator</p></div>
</body></html>"""

def generate():
    t = Template(HTML_TPL)
    html = t.render(
        date=datetime.now().strftime("%d %b %Y"),
        user_name=USER["name"],
        user_login=USER["login"],
        public=STATS["public"],
        private=STATS["private"],
        size=STATS["size"],
        repos=REPOS
    )
    HTML(string=html).write_pdf("repositorios_github.pdf")
    return "✅ PDF generado: repositorios_github.pdf"

if __name__ == "__main__":
    print(generate())
