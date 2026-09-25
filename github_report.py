#!/usr/bin/env python3
"""
GitHub Repositories Professional PDF Report Generator
Ephemeral script using WeasyPrint + Jinja2
Size: ~4.5 KB | Optimized for sandbox execution
"""

from datetime import datetime
from jinja2 import Template
from weasyprint import HTML

# User and repository data
USER = {"name": "Gloria Peralta", "login": "gloriaperaltav"}
REPOS = [
    {
        "name": "qa_cypress_orion",
        "language": "TypeScript",
        "stars": 0,
        "updated": "12 Mar 2025",
        "url": "https://github.com/gloriaperaltav/qa_cypress_orion"
    },
    {
        "name": "TEST",
        "language": "—",
        "stars": 0,
        "updated": "4 Sep 2026",
        "url": "https://github.com/gloriaperaltav/TEST"
    }
]
STATS = {"public": 2, "private": 0, "size": "3.7 KB"}

# Professional HTML template with GitHub styling
TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Informe de Repositorios GitHub</title>
    <style>
        @page { size: A4; margin: 2cm; }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; color: #24292e; line-height: 1.6; }
        
        .header { border-bottom: 3px solid #0366d6; padding-bottom: 20px; margin-bottom: 30px; }
        .header h1 { color: #0366d6; font-size: 28px; margin-bottom: 5px; }
        .header p { color: #586069; font-size: 13px; }
        
        .user-info { background: #f6f8fa; border-left: 4px solid #0366d6; padding: 15px; margin-bottom: 30px; border-radius: 3px; }
        .user-info h2 { color: #0366d6; font-size: 15px; margin-bottom: 8px; }
        .user-info p { font-size: 12px; color: #586069; margin: 4px 0; }
        
        .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 30px; }
        .stat-card { background: #f6f8fa; border: 1px solid #e1e4e8; padding: 15px; border-radius: 6px; text-align: center; }
        .stat-card .num { font-size: 24px; font-weight: bold; color: #0366d6; margin-bottom: 5px; }
        .stat-card .lbl { font-size: 11px; color: #586069; text-transform: uppercase; letter-spacing: 0.5px; }
        
        .section { color: #0366d6; font-size: 18px; font-weight: 600; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #e1e4e8; padding-bottom: 10px; }
        
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 12px; }
        thead { background: #f6f8fa; border-bottom: 2px solid #0366d6; }
        th { padding: 12px; text-align: left; font-weight: 600; color: #0366d6; }
        td { padding: 12px; border-bottom: 1px solid #e1e4e8; }
        tbody tr:hover { background: #f6f8fa; }
        
        .repo { background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px; padding: 15px; margin-bottom: 15px; }
        .repo h3 { color: #0366d6; font-size: 14px; margin-bottom: 8px; }
        .repo .meta { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; font-size: 11px; color: #586069; }
        .repo .meta strong { color: #24292e; margin-right: 5px; }
        
        .footer { margin-top: 40px; padding-top: 15px; border-top: 1px solid #e1e4e8; text-align: center; font-size: 10px; color: #6a737d; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Informe de Repositorios GitHub</h1>
        <p>{{ date }} | {{ user_name }} (@{{ user_login }})</p>
    </div>
    
    <div class="user-info">
        <h2>👤 Usuario</h2>
        <p><strong>Nombre:</strong> {{ user_name }}</p>
        <p><strong>Login:</strong> @{{ user_login }}</p>
    </div>
    
    <div class="stats-grid">
        <div class="stat-card">
            <div class="num">{{ public }}</div>
            <div class="lbl">Públicos</div>
        </div>
        <div class="stat-card">
            <div class="num">{{ private }}</div>
            <div class="lbl">Privados</div>
        </div>
        <div class="stat-card">
            <div class="num">{{ size }}</div>
            <div class="lbl">Tamaño Total</div>
        </div>
    </div>
    
    <h2 class="section">📦 Resumen de Repositorios</h2>
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Lenguaje</th>
                <th>⭐ Estrellas</th>
                <th>Actualizado</th>
            </tr>
        </thead>
        <tbody>
            {% for repo in repos %}
            <tr>
                <td><strong>{{ repo.name }}</strong></td>
                <td>{{ repo.language }}</td>
                <td>{{ repo.stars }}</td>
                <td>{{ repo.updated }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <h2 class="section">🔍 Detalles de Repositorios</h2>
    {% for repo in repos %}
    <div class="repo">
        <h3>{{ repo.name }}</h3>
        <div class="meta">
            <div><strong>Lenguaje:</strong> {{ repo.language }}</div>
            <div><strong>Estrellas:</strong> {{ repo.stars }}</div>
            <div><strong>Actualizado:</strong> {{ repo.updated }}</div>
            <div><strong>URL:</strong> <a href="{{ repo.url }}">GitHub</a></div>
        </div>
    </div>
    {% endfor %}
    
    <div class="footer">
        <p>Informe generado automáticamente | GitHub Repositories Report Generator</p>
    </div>
</body>
</html>"""

def generate_pdf():
    """Generate professional PDF report from repository data."""
    template = Template(TEMPLATE)
    html_content = template.render(
        date=datetime.now().strftime("%d de %B de %Y"),
        user_name=USER["name"],
        user_login=USER["login"],
        public=STATS["public"],
        private=STATS["private"],
        size=STATS["size"],
        repos=REPOS
    )
    HTML(string=html_content).write_pdf("repositorios_github.pdf")
    return "✅ PDF generado exitosamente: repositorios_github.pdf"

if __name__ == "__main__":
    print(generate_pdf())
