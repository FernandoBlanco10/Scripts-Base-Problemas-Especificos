# 🐍 Guía de comandos `pip` para Python

`pip` es el gestor de paquetes de Python que permite instalar, actualizar y eliminar librerías y dependencias.

---

## 1. Ver versión de pip

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `pip --version` | Muestra la versión instalada de pip | `pip --version` |

---

## 2. Instalar librerías

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `pip install <paquete>` | Instala la última versión de un paquete | `pip install requests` |
| `pip install <paquete>==<versión>` | Instala una versión específica de un paquete | `pip install numpy==1.25.0` |
| `pip install --upgrade <paquete>` | Actualiza un paquete a la última versión | `pip install --upgrade pandas` |
| `pip install -r requirements.txt` | Instala todos los paquetes listados en un archivo de requisitos | `pip install -r requirements.txt` |
| `pip install --user <paquete>` | Instala el paquete solo para el usuario actual (sin permisos de administrador) | `pip install --user flask` |

---

## 3. Desinstalar paquetes

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `pip uninstall <paquete>` | Elimina un paquete instalado | `pip uninstall requests` |

---

## 4. Listar paquetes instalados

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `pip list` | Lista todos los paquetes instalados con sus versiones | `pip list` |
| `pip show <paquete>` | Muestra información detallada de un paquete | `pip show flask` |
| `pip freeze` | Lista paquetes instalados en un formato compatible con `requirements.txt` | `pip freeze > requirements.txt` |

---

## 5. Buscar paquetes

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `pip search <paquete>` | Busca paquetes en el repositorio PyPI | `pip search requests` |

> ⚠️ Nota: `pip search` puede estar deshabilitado en algunas versiones recientes de pip; en su lugar, usar [https://pypi.org](https://pypi.org) para buscar paquetes.

---

## 6. Configuración y ayuda

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `pip help` | Muestra la ayuda general de pip | `pip help` |
| `pip install --help` | Muestra opciones de instalación | `pip install --help` |
| `pip config list` | Lista la configuración actual de pip | `pip config list` |
| `pip config set global.index-url <url>` | Cambia el repositorio PyPI por defecto | `pip config set global.index-url https://pypi.org/simple` |

---

## 7. Gestión de entornos

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| `python -m venv <entorno>` | Crea un entorno virtual | `python -m venv venv` |
| `source <entorno>/bin/activate` (Linux/Mac) o `<entorno>\Scripts\activate` (Windows) | Activa el entorno virtual | `venv\Scripts\activate` |
| `deactivate` | Desactiva el entorno virtual | `deactivate` |

---

## 8. Buenas prácticas

1. Usar **entornos virtuales** (`venv`) para proyectos independientes.  
2. Mantener un archivo `requirements.txt` para replicar dependencias.  
3. Actualizar pip regularmente:
   ```bash
   pip install --upgrade pip


# 🐍 Cheat Sheet de pip — Opciones y usos

| Opción / Flag | Significado | Ejemplo | Por qué se utiliza |
|---------------|------------|---------|------------------|
| `-m` | Ejecutar pip como módulo de Python | `python -m pip install requests` | Garantiza usar la versión de pip asociada al Python que estás ejecutando, evitando conflictos de versiones. |
| `-r` | Instalar desde archivo requirements | `pip install -r requirements.txt` | Permite instalar múltiples dependencias de un proyecto de manera ordenada y reproducible. |
| `-t` | Instalar en un directorio específico | `pip install -t ./libs requests` | Útil para empaquetar dependencias dentro de un proyecto o en un directorio personalizado. |
| `-U` / `--upgrade` | Actualizar paquete a la última versión | `pip install -U pandas` | Mantiene los paquetes actualizados con la última versión disponible. |
| `--user` | Instalar paquete solo para el usuario actual | `pip install --user flask` | Evita necesidad de permisos de administrador y mantiene el entorno de usuario aislado. |
| `--upgrade-strategy` | Define estrategia de actualización | `pip install -U --upgrade-strategy only-if-needed numpy` | Controla si se actualizan dependencias o solo el paquete principal. |
| `--no-cache-dir` | No usar caché de paquetes | `pip install --no-cache-dir package` | Evita problemas con paquetes corruptos o descargas de versiones antiguas en caché. |
| `--pre` | Instalar versiones pre-lanzamiento | `pip install --pre package` | Permite instalar versiones alpha, beta o RC de un paquete. |
| `--index-url` | Especificar repositorio PyPI | `pip install --index-url https://pypi.org/simple package` | Cambia el repositorio desde donde se descargan los paquetes. |
| `--trusted-host` | Agregar host confiable | `pip install --trusted-host pypi.org package` | Evita errores de certificado SSL con repositorios confiables. |
| `--find-links` | Buscar paquetes en carpeta o URL específica | `pip install --find-links ./libs package` | Útil para instalaciones offline o repositorios internos. |
| `--target` | Directorio de instalación personalizado | `pip install --target=./libs package` | Similar a `-t`, para incluir dependencias dentro del proyecto. |
| `--requirement` | Otra forma de usar `-r` | `pip install --requirement requirements.txt` | Instalación de múltiples paquetes desde archivo de dependencias. |
| `--upgrade` | Sinónimo de `-U` | `pip install --upgrade package` | Asegura que el paquete se actualice a la última versión disponible. |
| `--verbose` | Mostrar detalles de instalación | `pip install --verbose package` | Permite depurar problemas durante la instalación. |
| `--force-reinstall` | Reinstalar incluso si ya está instalado | `pip install --force-reinstall package` | Útil para corregir instalaciones corruptas o paquetes dañados. |
| `--disable-pip-version-check` | Deshabilitar chequeo de versión | `pip install --disable-pip-version-check package` | Evita retrasos en entornos con muchas instalaciones automáticas. |

---

## 💡 Consejos prácticos

1. **Usa `python -m pip` siempre que puedas** para evitar conflictos de versiones.  
2. **Usa entornos virtuales** (`venv`) para proyectos independientes.  
3. **Mantén un `requirements.txt`** para replicar dependencias.  
4. Para problemas con certificados SSL, combina `--trusted-host` y `--index-url`.  
5. Para instalaciones offline, usa `--find-links` o `--target` dentro del proyecto.  

