# 🐧 Cheat Sheet de Comandos Linux

Este documento incluye los comandos más comunes de Linux, organizados por categoría.

---

## 1. Navegación de directorios

| Comando | Significado / Acción | Ejemplo | Por qué se utiliza |
|---------|-------------------|---------|------------------|
| `pwd` | Mostrar directorio actual | `pwd` | Saber en qué ruta estás trabajando. |
| `ls` | Listar archivos y carpetas | `ls -l` | Ver contenido de un directorio con detalles. |
| `cd` | Cambiar de directorio | `cd /home/usuario` | Navegar entre carpetas. |
| `tree` | Mostrar estructura de carpetas | `tree -L 2` | Visualizar jerarquía de carpetas. |

---

## 2. Gestión de archivos y carpetas

| Comando | Significado / Acción | Ejemplo | Por qué se utiliza |
|---------|-------------------|---------|------------------|
| `cp` | Copiar archivos o carpetas | `cp archivo.txt /home/usuario/` | Duplicar archivos o moverlos temporalmente. |
| `mv` | Mover o renombrar archivos | `mv archivo.txt nuevo_nombre.txt` | Cambiar ubicación o nombre de un archivo. |
| `rm` | Eliminar archivos | `rm archivo.txt` | Borrar archivos de forma permanente. |
| `rmdir` | Eliminar carpetas vacías | `rmdir carpeta` | Limpiar directorios vacíos. |
| `mkdir` | Crear directorios | `mkdir nueva_carpeta` | Crear nuevas carpetas para organizar archivos. |
| `touch` | Crear archivo vacío | `touch nuevo.txt` | Crear archivos rápidamente. |

---

## 3. Visualización de contenido

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `cat` | Mostrar contenido de un archivo | `cat archivo.txt` | Ver rápidamente el contenido de un archivo. |
| `less` | Ver archivo página por página | `less archivo.txt` | Navegar archivos largos sin abrir un editor. |
| `head` | Mostrar primeras líneas | `head -n 10 archivo.txt` | Ver inicio del archivo. |
| `tail` | Mostrar últimas líneas | `tail -n 10 archivo.txt` | Ver el final del archivo o logs. |
| `tail -f` | Ver archivo en tiempo real | `tail -f /var/log/syslog` | Monitorizar logs en vivo. |

---

## 4. Permisos y propietario

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `chmod` | Cambiar permisos de archivo | `chmod 755 script.sh` | Definir quién puede leer, escribir o ejecutar. |
| `chown` | Cambiar propietario | `chown usuario:grupo archivo.txt` | Ajustar propietario y grupo de archivos. |
| `sudo` | Ejecutar comandos como superusuario | `sudo apt update` | Ejecutar tareas que requieren permisos de root. |

---

## 5. Procesos y recursos

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `ps` | Ver procesos en ejecución | `ps aux` | Listar todos los procesos activos. |
| `top` | Monitor de procesos en tiempo real | `top` | Revisar uso de CPU, memoria y procesos. |
| `kill` | Terminar un proceso | `kill 1234` | Detener procesos problemáticos por su PID. |
| `htop` | Monitor interactivo | `htop` | Similar a `top` pero más visual e interactivo. |

---

## 6. Redes y conectividad

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `ping` | Verificar conexión a host | `ping google.com` | Diagnosticar conectividad de red. |
| `ifconfig` / `ip a` | Mostrar interfaces de red | `ip a` | Revisar IPs y configuración de red. |
| `netstat` | Ver conexiones y puertos | `netstat -tulnp` | Ver puertos abiertos y servicios escuchando. |
| `curl` | Hacer peticiones HTTP | `curl https://example.com` | Probar servidores y APIs desde la terminal. |
| `wget` | Descargar archivos | `wget https://example.com/archivo.zip` | Descargar archivos desde internet. |

---

## 7. Buscar archivos y contenido

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `find` | Buscar archivos o carpetas | `find /home -name archivo.txt` | Localizar archivos por nombre. |
| `grep` | Buscar texto dentro de archivos | `grep "error" archivo.log` | Filtrar contenido de archivos. |
| `locate` | Buscar archivos rápidamente (usa base de datos) | `locate archivo.txt` | Buscar archivos sin recorrer directorio en tiempo real. |

---

## 8. Comprimir y descomprimir

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `tar -cvf` | Comprimir a tar | `tar -cvf backup.tar carpeta/` | Crear archivo tar de una carpeta. |
| `tar -xvf` | Descomprimir tar | `tar -xvf backup.tar` | Extraer archivos de un tar. |
| `zip` | Comprimir a zip | `zip -r backup.zip carpeta/` | Comprimir carpetas en formato zip. |
| `unzip` | Descomprimir zip | `unzip backup.zip` | Extraer archivos de zip. |

---

## 9. Actualización y gestión de paquetes (Debian/Ubuntu)

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `sudo apt update` | Actualizar lista de paquetes | `sudo apt update` | Obtener la lista más reciente de paquetes disponibles. |
| `sudo apt upgrade` | Actualizar paquetes instalados | `sudo apt upgrade` | Instalar las últimas versiones de los paquetes. |
| `sudo apt install` | Instalar paquete | `sudo apt install git` | Instalar nuevas aplicaciones o librerías. |
| `sudo apt remove` | Desinstalar paquete | `sudo apt remove nano` | Eliminar aplicaciones o librerías no deseadas. |

---

## 10. Sistema y disco

| Comando | Acción | Ejemplo | Por qué se utiliza |
|---------|-------|---------|------------------|
| `df -h` | Mostrar uso de disco | `df -h` | Ver espacio libre y usado en discos. |
| `du -sh` | Tamaño de carpeta | `du -sh /home/usuario` | Saber cuánto ocupa una carpeta. |
| `free -h` | Memoria disponible | `free -h` | Revisar uso de RAM y swap. |
| `uptime` | Tiempo de actividad | `uptime` | Ver cuánto tiempo lleva corriendo el sistema. |
| `who` | Usuarios conectados | `who` | Revisar quién está conectado al sistema. |

---

> 💡 **Consejo:** La combinación de comandos como `ls -lh`, `grep`, `find` y `tail -f` permite crear pipelines muy potentes para administración de sistemas.
