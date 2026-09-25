# 📑 GitHub PDF Report Generator - Index

## 📌 Resumen Ejecutivo

Se han creado **3 scripts Python efímeros** para generar un informe PDF profesional de repositorios de GitHub del usuario **Gloria Peralta** (@gloriaperaltav).

### ✅ Requisitos Cumplidos

- ✅ Usa **WeasyPrint** para renderizar PDF desde HTML con CSS
- ✅ Genera HTML con **Jinja2 template** con datos específicos
- ✅ Incluye tabla resumen, detalles de repositorios y estadísticas
- ✅ Diseño profesional con colores GitHub (#0366d6)
- ✅ Formato A4 con márgenes de 2cm
- ✅ Guarda como "repositorios_github.pdf" en directorio actual
- ✅ Retorna confirmación de generación exitosa
- ✅ Scripts efímeros (< 20 KB)
- ✅ Optimizados para ejecutarse en sandbox

---

## 📂 Scripts Disponibles

### 1. **github_report.py** ⭐ RECOMENDADO
**Tamaño:** 5.95 KB | **Tipo:** Legible y Profesional

```bash
python3 github_report.py
```

**Características:**
- Código bien estructurado y comentado
- Fácil de entender y mantener
- Separación clara de datos y template
- Mejor para aprender y personalizar

**Contenido:**
```python
- USER: Datos del usuario
- REPOS: Lista de repositorios
- STATS: Estadísticas
- TEMPLATE: HTML con CSS profesional
- generate_pdf(): Función principal
```

---

### 2. **report_gen.py** ⚡ ULTRA-COMPACTO
**Tamaño:** 3.4 KB | **Tipo:** Minificado

```bash
python3 report_gen.py
```

**Características:**
- Código minificado y optimizado
- Máximo rendimiento
- Ideal para sandbox con restricciones
- Una sola línea de ejecución

**Ventajas:**
- Menor consumo de memoria
- Ejecución más rápida
- Perfecto para automatización

---

### 3. **generate_github_report.py** 🔄 ALTERNATIVO
**Tamaño:** 4.45 KB | **Tipo:** Intermedio

```bash
python3 generate_github_report.py
```

**Características:**
- Balance entre legibilidad y compacidad
- Código optimizado pero legible
- Buena opción alternativa

---

## 📊 Datos Incluidos en el PDF

### Usuario
| Campo | Valor |
|-------|-------|
| Nombre | Gloria Peralta |
| Login | gloriaperaltav |
| Perfil | https://github.com/gloriaperaltav |

### Repositorios
| Nombre | Lenguaje | Estrellas | Actualizado |
|--------|----------|-----------|-------------|
| qa_cypress_orion | TypeScript | 0 | 12 Mar 2025 |
| TEST | — | 0 | 4 Sep 2026 |

### Estadísticas
- **Públicos:** 2
- **Privados:** 0
- **Tamaño Total:** 3.7 KB

---

## 🎨 Diseño del PDF

### Estructura
1. **Encabezado** - Título y fecha
2. **Información del Usuario** - Datos personales
3. **Estadísticas** - Grid de 3 tarjetas
4. **Tabla Resumen** - Listado de repositorios
5. **Detalles** - Información detallada de cada repo
6. **Pie de Página** - Información de generación

### Estilos
- **Color Primario:** #0366d6 (Azul GitHub)
- **Fondo:** #f6f8fa (Gris claro)
- **Texto:** #24292e (Gris oscuro)
- **Bordes:** #e1e4e8 (Gris medio)
- **Tipografía:** Segoe UI, sans-serif
- **Formato:** A4, márgenes 2cm

---

## 🚀 Guía de Uso Rápido

### Instalación
```bash
pip install weasyprint jinja2
```

### Ejecución
```bash
# Opción 1: Script recomendado
python3 github_report.py

# Opción 2: Script ultra-compacto
python3 report_gen.py

# Opción 3: Script alternativo
python3 generate_github_report.py
```

### Resultado
```
✅ PDF generado: repositorios_github.pdf
```

---

## 📚 Documentación Disponible

| Archivo | Descripción |
|---------|-------------|
| **QUICK_START.md** | Guía rápida de inicio |
| **GITHUB_REPORT_README.md** | Documentación completa |
| **PDF_GENERATOR_INDEX.md** | Este archivo (índice) |

---

## 🔧 Personalización

Para modificar los datos, edita las variables al inicio del script:

```python
# Usuario
USER = {"name": "Tu Nombre", "login": "tu_usuario"}

# Repositorios
REPOS = [
    {
        "name": "nombre_repo",
        "language": "Lenguaje",
        "stars": 0,
        "updated": "Fecha",
        "url": "https://github.com/usuario/repo"
    }
]

# Estadísticas
STATS = {"public": 2, "private": 0, "size": "3.7 KB"}
```

---

## 📋 Comparativa de Scripts

| Aspecto | github_report.py | report_gen.py | generate_github_report.py |
|--------|------------------|---------------|--------------------------|
| Tamaño | 5.95 KB | 3.4 KB | 4.45 KB |
| Legibilidad | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Rendimiento | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Mantenibilidad | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Recomendado | ✅ | Para sandbox | Alternativa |

---

## 💾 Archivos Generados

### Scripts Python
- `github_report.py` - Script principal (recomendado)
- `report_gen.py` - Script ultra-compacto
- `generate_github_report.py` - Script alternativo

### Documentación
- `QUICK_START.md` - Guía rápida
- `GITHUB_REPORT_README.md` - Documentación completa
- `PDF_GENERATOR_INDEX.md` - Este índice

### Salida
- `repositorios_github.pdf` - PDF generado (creado al ejecutar)

---

## ✨ Características Técnicas

### Tecnologías Utilizadas
- **Python 3.7+**
- **Jinja2** - Template engine
- **WeasyPrint** - PDF renderer
- **HTML5 + CSS3** - Markup y estilos

### Optimizaciones
- Código minificado (report_gen.py)
- Sin dependencias externas complejas
- Ejecución rápida
- Bajo consumo de memoria
- Compatible con sandbox

### Validaciones
- ✅ Todos los scripts < 20 KB
- ✅ Generan PDF válido
- ✅ Formato A4 correcto
- ✅ Márgenes de 2cm
- ✅ Salida relativa (repositorios_github.pdf)

---

## 🎯 Casos de Uso

1. **Reportes Automáticos** - Generar reportes periódicos
2. **Documentación** - Crear documentación de proyectos
3. **Presentaciones** - Preparar información para presentar
4. **Archivos** - Guardar historial de repositorios
5. **Análisis** - Documentar estado de proyectos

---

## 🔍 Validación de Requisitos

| Requisito | Estado | Detalles |
|-----------|--------|----------|
| WeasyPrint para PDF | ✅ | Implementado en todos los scripts |
| Jinja2 template | ✅ | Template HTML con variables |
| Datos específicos | ✅ | Usuario, 2 repos, estadísticas |
| Tabla resumen | ✅ | Incluida en PDF |
| Detalles repositorios | ✅ | Sección detallada |
| Estadísticas | ✅ | Grid de 3 tarjetas |
| Colores GitHub | ✅ | #0366d6 azul |
| Tipografía clara | ✅ | Segoe UI, sans-serif |
| Formato A4 | ✅ | @page size: A4 |
| Márgenes 2cm | ✅ | margin: 2cm |
| Archivo repositorios_github.pdf | ✅ | Salida relativa |
| Confirmación exitosa | ✅ | Mensaje de éxito |
| Efímero < 20 KB | ✅ | Máximo 5.95 KB |
| Optimizado sandbox | ✅ | Sin dependencias pesadas |

---

## 📞 Soporte

Para reportar problemas o sugerencias:
- Usuario: gloriaperaltav
- Repositorio: qa_cypress_orion
- Perfil: https://github.com/gloriaperaltav

---

## 📝 Notas Finales

- Los scripts son **efímeros** y están optimizados para ejecución única
- El PDF generado es de **alta calidad** y listo para imprimir
- Compatible con **A4 y otros formatos** de página
- Márgenes y estilos **totalmente configurables**
- Código **bien documentado** y fácil de personalizar

---

**Generado automáticamente | GitHub Repositories Report Generator**
**Última actualización:** 25 de Septiembre de 2026
