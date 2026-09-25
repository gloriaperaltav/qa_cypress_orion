#!/usr/bin/env python3
"""
GitHub Repositories Professional PDF Report Generator
Uses WeasyPrint + Jinja2 to create a styled PDF report
"""

from datetime import datetime
from jinja2 import Template
from weasyprint import HTML, CSS
import io

# Report data
user_data = {
    "username": "gloriaperaltav",
    "name": "Gloria Peralta",
    "generated_at": datetime.now().strftime("%d de %B de %Y"),
    "stats": {
        "public_repos": 2,
        "private_repos": 0,
        "total_stars": 0,
        "total_size_kb": 3.7
    }
}

repositories = [
    {
        "name": "qa_cypress_orion",
        "description": "Proyecto de automatización de pruebas con Cypress",
        "url": "https://github.com/gloriaperaltav/qa_cypress_orion",
        "language": "TypeScript",
        "stars": 0,
        "visibility": "Público",
        "updated_at": "12 Mar 2025"
    },
    {
        "name": "TEST",
        "description": "Repositorio de pruebas",
        "url": "https://github.com/gloriaperaltav/TEST",
        "language": "Sin especificar",
        "stars": 0,
        "visibility": "Público",
        "updated_at": "4 Sep 2026"
    }
]

# HTML Template with professional styling
html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe de Repositorios GitHub</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        @page {
            size: A4;
            margin: 2cm;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            line-height: 1.6;
            background: #f8f9fa;
        }
        
        .container {
            max-width: 210mm;
            background: white;
            padding: 2cm;
        }
        
        header {
            border-bottom: 3px solid #0366d6;
            padding-bottom: 1.5cm;
            margin-bottom: 1.5cm;
        }
        
        .header-title {
            font-size: 28px;
            font-weight: 700;
            color: #0366d6;
            margin-bottom: 0.5cm;
        }
        
        .header-subtitle {
            font-size: 14px;
            color: #666;
            margin-bottom: 0.3cm;
        }
        
        .header-meta {
            font-size: 12px;
            color: #999;
        }
        
        .stats-section {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1cm;
            margin-bottom: 2cm;
            padding: 1cm;
            background: #f6f8fa;
            border-radius: 6px;
        }
        
        .stat-card {
            text-align: center;
            padding: 0.8cm;
            background: white;
            border-left: 4px solid #0366d6;
            border-radius: 4px;
        }
        
        .stat-value {
            font-size: 24px;
            font-weight: 700;
            color: #0366d6;
            margin-bottom: 0.3cm;
        }
        
        .stat-label {
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .section-title {
            font-size: 18px;
            font-weight: 700;
            color: #0366d6;
            margin-top: 1.5cm;
            margin-bottom: 1cm;
            padding-bottom: 0.5cm;
            border-bottom: 2px solid #e1e4e8;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1.5cm;
            font-size: 11px;
        }
        
        thead {
            background: #f6f8fa;
            border-bottom: 2px solid #0366d6;
        }
        
        th {
            padding: 0.6cm;
            text-align: left;
            font-weight: 700;
            color: #0366d6;
            text-transform: uppercase;
            font-size: 10px;
            letter-spacing: 0.5px;
        }
        
        td {
            padding: 0.6cm;
            border-bottom: 1px solid #e1e4e8;
        }
        
        tbody tr:nth-child(even) {
            background: #f6f8fa;
        }
        
        tbody tr:hover {
            background: #f0f4f8;
        }
        
        .repo-name {
            font-weight: 600;
            color: #0366d6;
        }
        
        .language-badge {
            display: inline-block;
            padding: 0.2cm 0.4cm;
            background: #0366d6;
            color: white;
            border-radius: 3px;
            font-size: 10px;
            font-weight: 600;
        }
        
        .visibility-badge {
            display: inline-block;
            padding: 0.2cm 0.4cm;
            background: #28a745;
            color: white;
            border-radius: 3px;
            font-size: 10px;
            font-weight: 600;
        }
        
        .repo-details {
            margin-bottom: 2cm;
            padding: 1cm;
            background: #f6f8fa;
            border-left: 4px solid #0366d6;
            border-radius: 4px;
            page-break-inside: avoid;
        }
        
        .repo-details-title {
            font-size: 14px;
            font-weight: 700;
            color: #0366d6;
            margin-bottom: 0.5cm;
        }
        
        .repo-details-item {
            margin-bottom: 0.4cm;
            font-size: 11px;
        }
        
        .repo-details-label {
            font-weight: 600;
            color: #666;
            display: inline-block;
            width: 3cm;
        }
        
        .repo-details-value {
            color: #333;
        }
        
        footer {
            margin-top: 2cm;
            padding-top: 1cm;
            border-top: 1px solid #e1e4e8;
            text-align: center;
            font-size: 10px;
            color: #999;
        }
        
        .url-link {
            color: #0366d6;
            text-decoration: none;
            word-break: break-all;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-title">📊 Informe de Repositorios GitHub</div>
            <div class="header-subtitle">Usuario: {{ username }} ({{ name }})</div>
            <div class="header-meta">Generado: {{ generated_at }}</div>
        </header>
        
        <section class="stats-section">
            <div class="stat-card">
                <div class="stat-value">{{ stats.public_repos }}</div>
                <div class="stat-label">Públicos</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ stats.private_repos }}</div>
                <div class="stat-label">Privados</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ stats.total_stars }}</div>
                <div class="stat-label">Estrellas</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ stats.total_size_kb }}</div>
                <div class="stat-label">KB Totales</div>
            </div>
        </section>
        
        <h2 class="section-title">Resumen de Repositorios</h2>
        <table>
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Lenguaje</th>
                    <th>Estrellas</th>
                    <th>Visibilidad</th>
                    <th>Última Actualización</th>
                </tr>
            </thead>
            <tbody>
                {% for repo in repositories %}
                <tr>
                    <td><span class="repo-name">{{ repo.name }}</span></td>
                    <td><span class="language-badge">{{ repo.language }}</span></td>
                    <td>⭐ {{ repo.stars }}</td>
                    <td><span class="visibility-badge">{{ repo.visibility }}</span></td>
                    <td>{{ repo.updated_at }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        
        <h2 class="section-title">Detalles de Repositorios</h2>
        {% for repo in repositories %}
        <div class="repo-details">
            <div class="repo-details-title">{{ repo.name }}</div>
            <div class="repo-details-item">
                <span class="repo-details-label">Descripción:</span>
                <span class="repo-details-value">{{ repo.description }}</span>
            </div>
            <div class="repo-details-item">
                <span class="repo-details-label">URL:</span>
                <span class="repo-details-value"><a href="{{ repo.url }}" class="url-link">{{ repo.url }}</a></span>
            </div>
            <div class="repo-details-item">
                <span class="repo-details-label">Lenguaje:</span>
                <span class="repo-details-value">{{ repo.language }}</span>
            </div>
            <div class="repo-details-item">
                <span class="repo-details-label">Estrellas:</span>
                <span class="repo-details-value">{{ repo.stars }}</span>
            </div>
            <div class="repo-details-item">
                <span class="repo-details-label">Visibilidad:</span>
                <span class="repo-details-value">{{ repo.visibility }}</span>
            </div>
            <div class="repo-details-item">
                <span class="repo-details-label">Actualizado:</span>
                <span class="repo-details-value">{{ repo.updated_at }}</span>
            </div>
        </div>
        {% endfor %}
        
        <footer>
            <p>Informe generado automáticamente | GitHub Repositories Report Generator</p>
        </footer>
    </div>
</body>
</html>
"""

def generate_pdf():
    """Generate PDF report from template and data"""
    try:
        # Render template
        template = Template(html_template)
        html_content = template.render(
            username=user_data["username"],
            name=user_data["name"],
            generated_at=user_data["generated_at"],
            stats=user_data["stats"],
            repositories=repositories
        )
        
        # Generate PDF
        HTML(string=html_content).write_pdf("repositorios_github.pdf")
        
        return {
            "success": True,
            "message": "PDF generado exitosamente",
            "file": "repositorios_github.pdf",
            "repos_count": len(repositories),
            "file_size": "~150 KB"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    result = generate_pdf()
    if result["success"]:
        print(f"✅ {result['message']}")
        print(f"📄 Archivo: {result['file']}")
        print(f"📊 Repositorios incluidos: {result['repos_count']}")
        print(f"💾 Tamaño aproximado: {result['file_size']}")
    else:
        print(f"❌ Error: {result['error']}")
