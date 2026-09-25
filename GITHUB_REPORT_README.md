# 📊 GitHub Repositories PDF Report Generator

Script efímero profesional para generar reportes en PDF de repositorios de GitHub.

## 📋 Descripción

Genera un informe PDF profesional con los datos de repositorios de GitHub del usuario **gloriaperaltav** (Gloria Peralta).

### Características

✅ **Diseño Profesional**
- Colores GitHub (#0366d6 azul)
- Tipografía clara y legible
- Formato A4 con márgenes de 2cm
- Responsive y optimizado para impresión

✅ **Contenido Incluido**
- Información del usuario
- Tabla resumen de repositorios
- Detalles individuales de cada repositorio
- Estadísticas (públicos, privados, tamaño total)

✅ **Optimizado**
- Tamaño: ~6 KB (efímero)
- Usa WeasyPrint + Jinja2
- Ejecutable en sandbox
- Sin dependencias externas complejas

## 📦 Repositorios Incluidos

| Nombre | Lenguaje | Estrellas | Actualizado |
|--------|----------|-----------|-------------|
| qa_cypress_orion | TypeScript | 0 | 12 Mar 2025 |
| TEST | — | 0 | 4 Sep 2026 |

**Estadísticas:**
- 2 repositorios públicos
- 0 repositorios privados
- 3.7 KB tamaño total

## 🚀 Uso

### Opción 1: Script Principal (Recomendado)
```bash
python3 github_report.py
```

### Opción 2: Script Ultra-Compacto
```bash
python3 report_gen.py
```

### Opción 3: Script Optimizado
```bash
python3 generate_github_report.py
```

## 📄 Salida

El script genera un archivo PDF:
```
repositorios_github.pdf
```

Ubicación: Directorio actual (salida relativa)

## 🛠️ Requisitos

```bash
pip install weasyprint jinja2
```

### Dependencias del Sistema
- Python 3.7+
- WeasyPrint (requiere librerías de renderizado)

## 📝 Estructura del Informe

1. **Encabezado**
   - Título: "Informe de Repositorios GitHub"
   - Fecha de generación
   - Usuario y login

2. **Información del Usuario**
   - Nombre completo
   - Login de GitHub

3. **Estadísticas**
   - Repositorios públicos
   - Repositorios privados
   - Tamaño total

4. **Tabla Resumen**
   - Nombre del repositorio
   - Lenguaje de programación
   - Número de estrellas
   - Fecha de última actualización

5. **Detalles de Repositorios**
   - Información detallada de cada repositorio
   - Lenguaje, estrellas, fecha de actualización
   - URL del repositorio

6. **Pie de Página**
   - Información de generación automática

## 🎨 Estilos

- **Color Primario:** #0366d6 (Azul GitHub)
- **Fondo:** #f6f8fa (Gris claro)
- **Texto:** #24292e (Gris oscuro)
- **Bordes:** #e1e4e8 (Gris medio)

## 📊 Datos Incluidos

### Usuario
- **Nombre:** Gloria Peralta
- **Login:** gloriaperaltav
- **Perfil:** https://github.com/gloriaperaltav

### Repositorio 1: qa_cypress_orion
- **Lenguaje:** TypeScript
- **Estrellas:** 0
- **Visibilidad:** Público
- **Actualizado:** 12 Mar 2025
- **URL:** https://github.com/gloriaperaltav/qa_cypress_orion

### Repositorio 2: TEST
- **Lenguaje:** No especificado
- **Estrellas:** 0
- **Visibilidad:** Público
- **Actualizado:** 4 Sep 2026
- **URL:** https://github.com/gloriaperaltav/TEST

## 💾 Tamaño del Script

| Script | Tamaño |
|--------|--------|
| github_report.py | ~6 KB |
| report_gen.py | ~3.4 KB |
| generate_github_report.py | ~4.5 KB |

Todos son **efímeros** (< 20 KB) y optimizados para ejecución en sandbox.

## ✨ Características Técnicas

- **Template Engine:** Jinja2
- **PDF Renderer:** WeasyPrint
- **Formato:** HTML5 + CSS3
- **Codificación:** UTF-8
- **Idioma:** Español

## 🔧 Personalización

Para modificar los datos, edita las variables al inicio del script:

```python
USER = {"name": "Nombre", "login": "usuario"}
REPOS = [...]
STATS = {"public": 2, "private": 0, "size": "3.7 KB"}
```

## 📋 Notas

- El script es **efímero** y está optimizado para ejecutarse una sola vez
- Genera un PDF de alta calidad listo para imprimir
- Compatible con A4 y otros formatos de página
- Márgenes configurables (actualmente 2cm)

## 📞 Soporte

Para reportar problemas o sugerencias, contacta al usuario gloriaperaltav.

---

**Generado automáticamente | GitHub Repositories Report Generator**
