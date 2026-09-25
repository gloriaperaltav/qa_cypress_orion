# 🚀 Quick Start - GitHub PDF Report Generator

## Instalación Rápida

```bash
# 1. Instalar dependencias
pip install weasyprint jinja2

# 2. Ejecutar el script
python3 github_report.py

# 3. Abrir el PDF generado
open repositorios_github.pdf  # macOS
xdg-open repositorios_github.pdf  # Linux
start repositorios_github.pdf  # Windows
```

## ¿Qué Genera?

Un archivo PDF profesional: **repositorios_github.pdf**

### Contenido del PDF:
- 📊 Informe de repositorios de Gloria Peralta
- 📦 Tabla resumen con 2 repositorios
- 🔍 Detalles de cada repositorio
- 📈 Estadísticas (2 públicos, 0 privados, 3.7 KB)
- 🎨 Diseño profesional con colores GitHub

## Scripts Disponibles

### 1. **github_report.py** (Recomendado)
- Tamaño: ~6 KB
- Más legible y mantenible
- Mejor para entender el código

```bash
python3 github_report.py
```

### 2. **report_gen.py** (Ultra-Compacto)
- Tamaño: ~3.4 KB
- Minificado y optimizado
- Mejor para sandbox

```bash
python3 report_gen.py
```

### 3. **generate_github_report.py** (Alternativo)
- Tamaño: ~4.5 KB
- Versión intermedia
- Buen balance

```bash
python3 generate_github_report.py
```

## Datos Incluidos

**Usuario:** Gloria Peralta (@gloriaperaltav)

**Repositorios:**
1. **qa_cypress_orion** - TypeScript, 0 ⭐, Actualizado 12 Mar 2025
2. **TEST** - Sin especificar, 0 ⭐, Actualizado 4 Sep 2026

**Estadísticas:**
- 2 repositorios públicos
- 0 repositorios privados
- 3.7 KB tamaño total

## Características del PDF

✅ Formato A4 con márgenes de 2cm
✅ Colores GitHub (#0366d6 azul)
✅ Tipografía profesional
✅ Tabla resumen
✅ Detalles de cada repositorio
✅ Estadísticas
✅ Listo para imprimir

## Solución de Problemas

### Error: "No module named 'weasyprint'"
```bash
pip install weasyprint
```

### Error: "No module named 'jinja2'"
```bash
pip install jinja2
```

### El PDF no se genera
- Verifica que tienes permisos de escritura en el directorio
- Asegúrate de que las dependencias están instaladas
- Intenta ejecutar desde un directorio diferente

## Personalización

Para cambiar los datos, edita el script:

```python
USER = {"name": "Tu Nombre", "login": "tu_usuario"}
REPOS = [
    {
        "name": "repo_name",
        "language": "Python",
        "stars": 5,
        "updated": "25 Sep 2026",
        "url": "https://github.com/usuario/repo"
    }
]
STATS = {"public": 2, "private": 0, "size": "3.7 KB"}
```

## Ejecución en Sandbox

El script está optimizado para ejecutarse en sandbox:
- Tamaño < 20 KB ✅
- Sin dependencias complejas ✅
- Ejecución rápida ✅
- Salida relativa (repositorios_github.pdf) ✅

## Resultado Esperado

```
✅ PDF generado exitosamente: repositorios_github.pdf
```

El archivo se crea en el directorio actual.

---

**¡Listo! Tu informe PDF está generado.** 📄
