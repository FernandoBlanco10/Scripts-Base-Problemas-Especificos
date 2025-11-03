# Guía paso a paso: Git + GitHub

Este documento describe los pasos consecutivos para:

1. Inicializar un repositorio en GitHub  
2. Clonar un repositorio existente  
3. Actualizar un repositorio remoto  
4. Crear y gestionar ramas  

---

## 🧩 1. Inicializar un repositorio en GitHub

### Crear un nuevo repositorio desde cero

1. Ingresa a [GitHub → Crear nuevo repositorio](https://github.com/new).  
2. Coloca un nombre para tu repositorio (por ejemplo, `mi-proyecto`).  
3. **No marques** la opción “Initialize this repository with a README” si ya tienes archivos locales.  
4. Crea el repositorio (clic en **Create repository**).  
5. Abre tu terminal o CMD en la carpeta de tu proyecto:

   ```bash
   cd ruta/del/proyecto

Inicializa el repositorio en la carpeta de tu proyecto:
    
    git init

Agrega todos los archivos del proyecto al área de preparación:
    
    git add .

Crea tu primer commit con una descripción clara del cambio:
    
    git commit -m "Primer commit del proyecto"

Conecta el repositorio local con el remoto (reemplaza la URL con la de tu repositorio en GitHub):
    
    git remote add origin https://github.com/usuario/mi-proyecto.git

Envía tus archivos al repositorio remoto:
    
    git push -u origin main

Si Git te indica que la rama principal se llama master, usa:
    
    git push -u origin master


## 🧩 2. Clonar un repositorio de GitHub

1. Abre el repositorio en GitHub. 
2. Haz clic en el botón verde Code y copia la URL HTTPS (o SSH).

Abre una terminal y ve a la carpeta donde quieres descargar el proyecto:

    cd ruta/donde/quieres/clonar

Clona el repositorio:

    git clone https://github.com/usuario/mi-proyecto.git

Entra al directorio clonado:
    
    cd mi-proyecto

Verifica que el repositorio remoto está correctamente configurado:
    
    git remote -v

## 🧩 3. Actualizar un repositorio de GitHub

### Descargar los cambios más recientes (pull)

Asegúrate de estar en la rama que quieres actualizar:
    
    git branch

Si necesitas cambiar de rama:
    
    git checkout main

Descarga y fusiona los últimos cambios del repositorio remoto:
    
    git pull origin main

Si hiciste cambios locales, primero guarda tus modificaciones:
    
    git add .
    git commit -m "Guarda cambios locales antes del pull"
    git pull origin main

### Subir tus cambios al repositorio remoto

Verifica qué archivos cambiaste:

    git status

Agrega los cambios al área de preparación (staging):

    git add .

Crea un nuevo commit:

    git commit -m "Actualiza componente de autenticación"

Envía tus cambios a GitHub:

    git push origin main


## 🧩 4. Crear y gestionar ramas (branches)

Crear una nueva rama

    git branch nombre-rama

Cambiar a otra rama

    git checkout nombre-rama

Crear y cambiar a la rama en un solo paso

    git checkout -b nombre-rama

Subir una nueva rama a GitHub

    git push -u origin nombre-rama

### Fusionar una rama con main

Cambia a la rama principal:

    git checkout main

Actualiza main:

    git pull origin main

Fusiona la rama de trabajo:

    git merge nombre-rama

Sube los cambios fusionados:

    git push origin main

### Eliminar ramas

Eliminar una rama localmente:
    git branch -d nombre-rama

Eliminar una rama en el repositorio remoto:

    git push origin --delete nombre-rama

## Consejos finales

- Usa `git log --oneline --graph --decorate` para visualizar de forma clara la historia de tus commits.
- Antes de fusionar ramas, asegúrate de hacer git pull para evitar conflictos.






