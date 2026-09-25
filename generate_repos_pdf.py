#!/usr/bin/env python3
"""
Script efímero para generar PDF profesional de repositorios GitHub.
Datos hardcodeados, sin dependencias externas de archivos.
"""

from weasyprint import HTML, CSS
from io import BytesIO
from datetime import datetime

# Datos hardcodeados
TITULO = "Repositorios GitHub - Gloria Peralta (@gloriaperaltav)"
FECHA_GENERACION = "2026-09-25"
REPOSITORIOS = [
    {
        "nombre": "qa_cypress_orion",
        "url": "https://github.com/gloriaperaltav/qa_cypress_orion",
        "descripcion": "Proyecto de automatización de pruebas con Cypress y TypeScript para testing de aplicaciones web",
        "lenguaje": "TypeScript",
        "stars": 0,
        "ultima_actualizacion": "2025-03-12"
    },
    {
        "nombre": "TEST",
        "url": "https://github.com/gloriaperaltav/TEST",
        "descripcion": "Repositorio de prueba (vacío)",
        "lenguaje": "N/A",
        "stars": 0,
        "ultima_actualizacion": "2026-09-04"
    }
]

# Resumen
TOTAL_REPOS = len(REPOSITORIOS)
REPOS_CON_CONTENIDO = 1
LENGUAJES = "TypeScript"

# HTML con CSS embebido
html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITULO}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        @page {{
            size: A4;
            margin: 2cm;
            @bottom-center {{
                content: "Página " counter(page) " de " counter(pages);
                font-size: 10px;
                color: #666;
            }}
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            line-height: 1.6;
            background-color: #f9f9f9;
        }}
        
        .container {{
            max-width: 100%;
            padding: 0;
        }}
        
        header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 2.5cm;
            margin-bottom: 1.5cm;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        h1 {{
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 0.5cm;
            letter-spacing: 0.5px;
        }}
        
        .header-meta {{
            font-size: 12px;
            opacity: 0.9;
            display: flex;
            gap: 2cm;
        }}
        
        .header-meta span {{
            display: flex;
            align-items: center;
        }}
        
        .header-meta strong {{
            margin-right: 0.3cm;
        }}
        
        .content {{
            padding: 0 0.5cm;
        }}
        
        h2 {{
            color: #1e3c72;
            font-size: 18px;
            margin-top: 1.5cm;
            margin-bottom: 0.8cm;
            border-bottom: 3px solid #2a5298;
            padding-bottom: 0.4cm;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1.5cm;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        
        thead {{
            background-color: #2a5298;
            color: white;
        }}
        
        th {{
            padding: 0.8cm;
            text-align: left;
            font-weight: 600;
            font-size: 12px;
            letter-spacing: 0.5px;
            border: 1px solid #1e3c72;
        }}
        
        td {{
            padding: 0.7cm 0.8cm;
            border: 1px solid #e0e0e0;
            font-size: 11px;
        }}
        
        tbody tr:nth-child(odd) {{
            background-color: #f5f8fb;
        }}
        
        tbody tr:nth-child(even) {{
            background-color: #ffffff;
        }}
        
        tbody tr:hover {{
            background-color: #e8f0f7;
        }}
        
        a {{
            color: #2a5298;
            text-decoration: none;
            word-break: break-all;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        .resumen {{
            background: linear-gradient(135deg, #f5f8fb 0%, #e8f0f7 100%);
            border-left: 4px solid #2a5298;
            padding: 1cm;
            margin-top: 1.5cm;
            border-radius: 4px;
        }}
        
        .resumen h3 {{
            color: #1e3c72;
            font-size: 14px;
            margin-bottom: 0.5cm;
        }}
        
        .resumen-item {{
            display: flex;
            justify-content: space-between;
            padding: 0.3cm 0;
            font-size: 12px;
            border-bottom: 1px solid #d0d8e0;
        }}
        
        .resumen-item:last-child {{
            border-bottom: none;
        }}
        
        .resumen-label {{
            font-weight: 600;
            color: #1e3c72;
        }}
        
        .resumen-value {{
            color: #555;
        }}
        
        footer {{
            margin-top: 2cm;
            padding-top: 1cm;
            border-top: 1px solid #e0e0e0;
            text-align: center;
            font-size: 10px;
            color: #999;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{TITULO}</h1>
            <div class="header-meta">
                <span><strong>Fecha de generación:</strong> {FECHA_GENERACION}</span>
                <span><strong>Total de repositorios:</strong> {TOTAL_REPOS}</span>
            </div>
        </header>
        
        <div class="content">
            <h2>📊 Repositorios</h2>
            
            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>URL</th>
                        <th>Descripción</th>
                        <th>Lenguaje</th>
                        <th>Stars</th>
                        <th>Última Actualización</th>
                    </tr>
                </thead>
                <tbody>
"""

# Agregar filas de repositorios
for repo in REPOSITORIOS:
    html_content += f"""
                    <tr>
                        <td><strong>{repo['nombre']}</strong></td>
                        <td><a href="{repo['url']}" target="_blank">{repo['url']}</a></td>
                        <td>{repo['descripcion']}</td>
                        <td>{repo['lenguaje']}</td>
                        <td>{repo['stars']}</td>
                        <td>{repo['ultima_actualizacion']}</td>
                    </tr>
"""

html_content += """
                </tbody>
            </table>
            
            <div class="resumen">
                <h3>📈 Resumen</h3>
"""

html_content += f"""
                <div class="resumen-item">
                    <span class="resumen-label">Total de repositorios:</span>
                    <span class="resumen-value">{TOTAL_REPOS}</span>
                </div>
                <div class="resumen-item">
                    <span class="resumen-label">Repositorios con contenido:</span>
                    <span class="resumen-value">{REPOS_CON_CONTENIDO}</span>
                </div>
                <div class="resumen-item">
                    <span class="resumen-label">Lenguajes detectados:</span>
                    <span class="resumen-value">{LENGUAJES}</span>
                </div>
"""

html_content += """
            </div>
        </div>
        
        <footer>
            <p>Documento generado automáticamente | © 2026 Gloria Peralta</p>
        </footer>
    </div>
</body>
</html>
"""

# Generar PDF
try:
    HTML(string=html_content).write_pdf('repositorios.pdf')
    print("PDF generado exitosamente: repositorios.pdf")
except Exception as e:
    print(f"Error al generar PDF: {e}")
    exit(1)
