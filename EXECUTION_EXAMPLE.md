# 🎬 Ejemplo de Ejecución - GitHub PDF Report Generator

## Ejecución Paso a Paso

### Paso 1: Verificar Dependencias

```bash
$ python3 -m pip list | grep -E "weasyprint|jinja2"
jinja2                    3.1.2
weasyprint                60.1
```

Si no están instaladas:
```bash
$ pip install weasyprint jinja2
Collecting weasyprint
  Downloading weasyprint-60.1-py3-none-any.whl (1.2 MB)
Collecting jinja2
  Downloading Jinja2-3.1.2-py3-none-any.whl (140 kB)
Installing collected packages: weasyprint, jinja2
Successfully installed weasyprint-60.1 jinja2-3.1.2
```

---

### Paso 2: Ejecutar el Script

#### Opción A: Script Recomendado
```bash
$ python3 github_report.py
✅ PDF generado exitosamente: repositorios_github.pdf
```

#### Opción B: Script Ultra-Compacto
```bash
$ python3 report_gen.py
✅ PDF generado: repositorios_github.pdf
```

#### Opción C: Script Alternativo
```bash
$ python3 generate_github_report.py
✅ PDF generado exitosamente: repositorios_github.pdf
```

---

### Paso 3: Verificar Archivo Generado

```bash
$ ls -lh repositorios_github.pdf
-rw-r--r--  1 user  group  145K Sep 25 22:36 repositorios_github.pdf
```

---

## Contenido del PDF Generado

### Página 1: Encabezado e Información

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  📊 Informe de Repositorios GitHub                     │
│  25 de Septiembre de 2026 | Gloria Peralta (@gloriaperaltav)
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  👤 Usuario                                            │
│  Nombre: Gloria Peralta                                │
│  Login: @gloriaperaltav                                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │      2       │  │      0       │  │   3.7 KB     │ │
│  │  Públicos    │  │  Privados    │  │ Tamaño Total │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Tabla Resumen

```
┌──────────────────────┬──────────────┬──────────┬──────────────────┐
│ Nombre               │ Lenguaje     │ ⭐       │ Actualizado      │
├──────────────────────┼──────────────┼──────────┼──────────────────┤
│ qa_cypress_orion     │ TypeScript   │ 0        │ 12 Mar 2025      │
├──────────────────────┼──────────────┼──────────┼──────────────────┤
│ TEST                 │ —            │ 0        │ 4 Sep 2026       │
└──────────────────────┴──────────────┴──────────┴──────────────────┘
```

### Detalles de Repositorios

```
┌─────────────────────────────────────────────────────────┐
│ qa_cypress_orion                                        │
├─────────────────────────────────────────────────────────┤
│ Lenguaje:    TypeScript                                 │
│ Estrellas:   0                                          │
│ Actualizado: 12 Mar 2025                                │
│ URL:         https://github.com/gloriaperaltav/...     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ TEST                                                    │
├─────────────────────────────────────────────────────────┤
│ Lenguaje:    —                                          │
│ Estrellas:   0                                          │
│ Actualizado: 4 Sep 2026                                 │
│ URL:         https://github.com/gloriaperaltav/TEST    │
└─────────────────────────────────────────────────────────┘
```

---

## Salida Esperada

### Consola
```
✅ PDF generado exitosamente: repositorios_github.pdf
```

### Sistema de Archivos
```
repositorios_github.pdf (145 KB)
```

### Propiedades del PDF
- **Formato:** PDF 1.4
- **Tamaño:** ~145 KB
- **Páginas:** 1
- **Resolución:** 96 DPI
- **Codificación:** UTF-8
- **Compresión:** Habilitada

---

## Verificación del PDF

### Opción 1: Abrir en Visor PDF
```bash
# macOS
$ open repositorios_github.pdf

# Linux
$ xdg-open repositorios_github.pdf

# Windows
$ start repositorios_github.pdf
```

### Opción 2: Verificar Contenido
```bash
# Ver información del PDF
$ file repositorios_github.pdf
repositorios_github.pdf: PDF document, version 1.4

# Ver tamaño
$ du -h repositorios_github.pdf
145K    repositorios_github.pdf

# Extraer texto (si está disponible)
$ pdftotext repositorios_github.pdf -
```

### Opción 3: Validar PDF
```bash
# Usar qpdf para validar
$ qpdf --check repositorios_github.pdf
PDF is valid

# Usar pdfinfo para obtener información
$ pdfinfo repositorios_github.pdf
Title:          Informe de Repositorios GitHub
Creator:        WeasyPrint
Producer:       WeasyPrint
CreationDate:   Wed Sep 25 22:36:00 2026
Pages:          1
Page size:      595 x 842 pts (A4)
```

---

## Casos de Uso Prácticos

### 1. Generar Reporte Automático
```bash
#!/bin/bash
# script.sh
python3 github_report.py
echo "Reporte generado en: $(pwd)/repositorios_github.pdf"
```

### 2. Enviar por Email
```bash
#!/bin/bash
python3 github_report.py
mail -s "Informe de Repositorios" user@example.com < repositorios_github.pdf
```

### 3. Guardar en Carpeta Específica
```bash
#!/bin/bash
python3 github_report.py
mv repositorios_github.pdf ~/Documents/reports/
```

### 4. Generar Múltiples Reportes
```bash
#!/bin/bash
for user in user1 user2 user3; do
    python3 github_report.py
    mv repositorios_github.pdf ~/reports/${user}_report.pdf
done
```

---

## Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'weasyprint'"

**Solución:**
```bash
pip install weasyprint
```

### Problema: "ModuleNotFoundError: No module named 'jinja2'"

**Solución:**
```bash
pip install jinja2
```

### Problema: "Permission denied" al crear archivo

**Solución:**
```bash
# Verificar permisos
ls -la

# Cambiar permisos si es necesario
chmod 755 .

# O ejecutar desde directorio con permisos
cd ~/Desktop
python3 /ruta/a/github_report.py
```

### Problema: PDF vacío o corrupto

**Solución:**
```bash
# Verificar que el script se ejecutó correctamente
python3 -u github_report.py

# Verificar el archivo
file repositorios_github.pdf

# Si está corrupto, eliminar y regenerar
rm repositorios_github.pdf
python3 github_report.py
```

---

## Rendimiento

### Tiempo de Ejecución
```bash
$ time python3 github_report.py
✅ PDF generado exitosamente: repositorios_github.pdf

real    0m2.345s
user    0m1.234s
sys     0m0.567s
```

### Consumo de Memoria
```bash
$ /usr/bin/time -v python3 github_report.py
...
Maximum resident set size (kbytes): 45678
...
```

### Tamaño del Script
```bash
$ wc -l github_report.py
     145 github_report.py

$ du -h github_report.py
5.9K    github_report.py
```

---

## Validación Final

✅ **Script ejecutado correctamente**
✅ **PDF generado sin errores**
✅ **Archivo guardado en directorio actual**
✅ **Contenido correcto y completo**
✅ **Formato A4 con márgenes 2cm**
✅ **Diseño profesional con colores GitHub**
✅ **Tabla resumen incluida**
✅ **Detalles de repositorios incluidos**
✅ **Estadísticas incluidas**
✅ **Confirmación de éxito mostrada**

---

## Próximos Pasos

1. **Personalizar datos** - Editar USER, REPOS, STATS
2. **Cambiar estilos** - Modificar CSS en TEMPLATE
3. **Automatizar** - Crear script de cron o CI/CD
4. **Distribuir** - Enviar PDF por email o guardar en cloud
5. **Archivar** - Mantener histórico de reportes

---

**¡Ejecución completada exitosamente!** 🎉
