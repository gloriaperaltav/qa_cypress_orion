# 📋 Requisitos e Instalación

## 🔧 Requisitos del Sistema

### Python
- **Versión:** Python 3.7 o superior
- **Verificar:** `python3 --version`

```bash
$ python3 --version
Python 3.9.13
```

### Sistema Operativo
- ✅ macOS (10.14+)
- ✅ Linux (Ubuntu 18.04+, Debian 10+, etc.)
- ✅ Windows (10+)

### Espacio en Disco
- **Scripts:** ~15 KB
- **Dependencias:** ~50 MB
- **PDF generado:** ~150 KB
- **Total:** ~50 MB

### Memoria RAM
- **Mínimo:** 256 MB
- **Recomendado:** 512 MB
- **Consumo real:** ~45 MB

---

## 📦 Dependencias Python

### Paquetes Requeridos

```
weasyprint>=60.0
jinja2>=3.0
```

### Paquetes Opcionales

```
# Para validar PDF
qpdf>=10.0

# Para extraer texto de PDF
pdftotext (poppler-utils)
```

---

## 🚀 Instalación Rápida

### 1. Clonar o Descargar Repositorio

```bash
# Opción A: Clonar con Git
git clone https://github.com/gloriaperaltav/qa_cypress_orion.git
cd qa_cypress_orion

# Opción B: Descargar ZIP
# Descargar desde GitHub y extraer
```

### 2. Instalar Dependencias

```bash
# Opción A: Instalar con pip
pip install weasyprint jinja2

# Opción B: Instalar desde requirements.txt
pip install -r requirements.txt

# Opción C: Instalar con pip3
pip3 install weasyprint jinja2
```

### 3. Ejecutar Script

```bash
# Opción A: Script recomendado
python3 github_report.py

# Opción B: Script ultra-compacto
python3 report_gen.py

# Opción C: Script alternativo
python3 generate_github_report.py
```

### 4. Verificar Resultado

```bash
# Verificar que el PDF se generó
ls -lh repositorios_github.pdf

# Abrir el PDF
open repositorios_github.pdf  # macOS
xdg-open repositorios_github.pdf  # Linux
start repositorios_github.pdf  # Windows
```

---

## 📝 Instalación Detallada por Sistema Operativo

### macOS

#### 1. Verificar Python
```bash
python3 --version
# Python 3.9.13
```

#### 2. Instalar Dependencias
```bash
pip3 install weasyprint jinja2
```

#### 3. Ejecutar Script
```bash
python3 github_report.py
```

#### 4. Abrir PDF
```bash
open repositorios_github.pdf
```

---

### Linux (Ubuntu/Debian)

#### 1. Actualizar Sistema
```bash
sudo apt update
sudo apt upgrade
```

#### 2. Instalar Python
```bash
sudo apt install python3 python3-pip
python3 --version
```

#### 3. Instalar Dependencias
```bash
pip3 install weasyprint jinja2
```

#### 4. Ejecutar Script
```bash
python3 github_report.py
```

#### 5. Abrir PDF
```bash
xdg-open repositorios_github.pdf
```

---

### Windows

#### 1. Instalar Python
- Descargar desde https://www.python.org/downloads/
- Ejecutar instalador
- ✅ Marcar "Add Python to PATH"

#### 2. Verificar Instalación
```cmd
python --version
# Python 3.9.13
```

#### 3. Instalar Dependencias
```cmd
pip install weasyprint jinja2
```

#### 4. Ejecutar Script
```cmd
python github_report.py
```

#### 5. Abrir PDF
```cmd
start repositorios_github.pdf
```

---

## 🐍 Entorno Virtual (Recomendado)

### Crear Entorno Virtual

```bash
# Crear
python3 -m venv venv

# Activar
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Instalar Dependencias en Entorno Virtual

```bash
pip install weasyprint jinja2
```

### Ejecutar Script

```bash
python3 github_report.py
```

### Desactivar Entorno Virtual

```bash
deactivate
```

---

## 📋 Archivo requirements.txt

Crear archivo `requirements.txt`:

```
weasyprint==60.1
jinja2==3.1.2
```

Instalar desde archivo:

```bash
pip install -r requirements.txt
```

---

## ✅ Verificación de Instalación

### Verificar Python
```bash
python3 --version
# Python 3.7 o superior ✅
```

### Verificar pip
```bash
pip3 --version
# pip 21.0 o superior ✅
```

### Verificar Paquetes
```bash
pip3 list | grep -E "weasyprint|jinja2"
# jinja2                    3.1.2
# weasyprint                60.1
```

### Verificar Importación
```bash
python3 -c "import weasyprint; import jinja2; print('✅ Todas las dependencias instaladas')"
# ✅ Todas las dependencias instaladas
```

---

## 🔧 Solución de Problemas

### Error: "Python not found"

**Causa:** Python no está instalado o no está en PATH

**Solución:**
```bash
# Instalar Python desde https://www.python.org/downloads/
# O usar gestor de paquetes:

# macOS (Homebrew)
brew install python3

# Linux (Ubuntu/Debian)
sudo apt install python3

# Windows
# Descargar e instalar desde python.org
```

---

### Error: "pip: command not found"

**Causa:** pip no está instalado

**Solución:**
```bash
# Instalar pip
python3 -m ensurepip --upgrade

# O usar gestor de paquetes
# macOS
brew install python3

# Linux
sudo apt install python3-pip
```

---

### Error: "No module named 'weasyprint'"

**Causa:** weasyprint no está instalado

**Solución:**
```bash
pip3 install weasyprint
```

---

### Error: "No module named 'jinja2'"

**Causa:** jinja2 no está instalado

**Solución:**
```bash
pip3 install jinja2
```

---

### Error: "Permission denied"

**Causa:** Permisos insuficientes

**Solución:**
```bash
# Opción A: Usar sudo (no recomendado)
sudo pip3 install weasyprint jinja2

# Opción B: Instalar en usuario (recomendado)
pip3 install --user weasyprint jinja2

# Opción C: Usar entorno virtual (mejor)
python3 -m venv venv
source venv/bin/activate
pip install weasyprint jinja2
```

---

### Error: "WeasyPrint requires libffi"

**Causa:** Falta librería del sistema

**Solución:**
```bash
# macOS
brew install libffi

# Linux (Ubuntu/Debian)
sudo apt install libffi-dev

# Linux (Fedora/RHEL)
sudo dnf install libffi-devel
```

---

## 🎯 Verificación Final

Ejecutar este comando para verificar que todo está instalado:

```bash
python3 -c "
import sys
import weasyprint
import jinja2

print('✅ Python:', sys.version.split()[0])
print('✅ WeasyPrint:', weasyprint.__version__)
print('✅ Jinja2:', jinja2.__version__)
print('✅ Todas las dependencias están instaladas correctamente')
"
```

Salida esperada:
```
✅ Python: 3.9.13
✅ WeasyPrint: 60.1
✅ Jinja2: 3.1.2
✅ Todas las dependencias están instaladas correctamente
```

---

## 📊 Tabla de Compatibilidad

| Sistema | Python | pip | Estado |
|---------|--------|-----|--------|
| macOS 10.14+ | 3.7+ | ✅ | ✅ Soportado |
| Ubuntu 18.04+ | 3.7+ | ✅ | ✅ Soportado |
| Debian 10+ | 3.7+ | ✅ | ✅ Soportado |
| Windows 10+ | 3.7+ | ✅ | ✅ Soportado |
| CentOS 7+ | 3.7+ | ✅ | ✅ Soportado |

---

## 💾 Tamaño de Descargas

| Paquete | Tamaño |
|---------|--------|
| weasyprint | ~1.2 MB |
| jinja2 | ~140 KB |
| Dependencias | ~48 MB |
| **Total** | **~50 MB** |

---

## ⏱️ Tiempo de Instalación

| Paso | Tiempo |
|------|--------|
| Descargar Python | 2-5 min |
| Instalar Python | 1-2 min |
| Instalar pip | < 1 min |
| Instalar weasyprint | 2-3 min |
| Instalar jinja2 | < 1 min |
| **Total** | **5-12 min** |

---

## 🔐 Seguridad

### Verificar Integridad de Paquetes

```bash
# Verificar hash de paquetes
pip install --require-hashes weasyprint jinja2

# Usar requirements.txt con hashes
pip install -r requirements.txt --require-hashes
```

### Actualizar Paquetes

```bash
# Actualizar pip
pip install --upgrade pip

# Actualizar paquetes
pip install --upgrade weasyprint jinja2
```

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Python](https://docs.python.org/3/)
- [WeasyPrint](https://weasyprint.org/)
- [Jinja2](https://jinja.palletsprojects.com/)

### Tutoriales
- [Python Installation Guide](https://wiki.python.org/moin/BeginnersGuide/Download)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

## ✨ Próximos Pasos

1. ✅ Instalar dependencias
2. ✅ Ejecutar script
3. ✅ Verificar PDF generado
4. ✅ Personalizar datos (opcional)
5. ✅ Automatizar ejecución (opcional)

---

**¡Listo para usar!** 🚀
