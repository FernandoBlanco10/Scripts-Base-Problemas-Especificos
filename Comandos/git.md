# Comandos Git — Guía rápida

| 🧩 Comando | ⚙️ Acción que realiza | 💡 Ejemplo práctico |
|-------------|-----------------------|---------------------|
| `git --version` | Muestra la versión instalada de Git | `git --version` |
| `git config --global user.name "<tu_nombre>"` | Configura tu nombre de usuario global | `git config --global user.name "Fernando Blanco"` |
| `git config --global user.email "<tu_correo>"` | Configura tu correo global | `git config --global user.email "fernando@example.com"` |
| `git config --list` | Muestra la configuración actual de Git | `git config --list` |
| `git init` | Inicializa un nuevo repositorio local en la carpeta actual | `git init` |
| `git clone <url>` | Clona un repositorio remoto en tu máquina | `git clone https://github.com/usuario/proyecto.git` |
| `git status` | Muestra el estado de los archivos (cambios, staged, etc.) | `git status` |
| `git add <archivo>` | Agrega un archivo al área de staging | `git add index.html` |
| `git add .` | Agrega todos los cambios al staging | `git add .` |
| `git commit -m "<mensaje>"` | Guarda los cambios en el repositorio local con un mensaje | `git commit -m "Agrega nueva función de login"` |
| `git log` | Muestra el historial de commits | `git log` |
| `git log --oneline` | Muestra el historial resumido | `git log --oneline` |
| `git diff` | Muestra las diferencias entre archivos modificados y el último commit | `git diff` |
| `git branch` | Lista las ramas del repositorio | `git branch` |
| `git branch <nombre>` | Crea una nueva rama | `git branch feature/login` |
| `git checkout <rama>` | Cambia a otra rama | `git checkout main` |
| `git checkout -b <nombre>` | Crea y cambia a una nueva rama | `git checkout -b feature/api` |
| `git merge <rama>` | Fusiona una rama en la rama actual | `git merge feature/api` |
| `git pull` | Descarga y fusiona cambios desde el repositorio remoto | `git pull origin main` |
| `git fetch` | Descarga los cambios del remoto sin fusionarlos | `git fetch origin` |
| `git push` | Envía los commits locales al repositorio remoto | `git push origin main` |
| `git push -u origin <rama>` | Envía la rama actual al remoto y la vincula | `git push -u origin develop` |
| `git remote -v` | Muestra las URLs de los repositorios remotos | `git remote -v` |
| `git remote add origin <url>` | Asocia un repositorio remoto | `git remote add origin https://github.com/usuario/proyecto.git` |
| `git reset <archivo>` | Quita un archivo del área de staging | `git reset index.html` |
| `git reset --hard HEAD` | Revierte todos los cambios locales al último commit | `git reset --hard HEAD` |
| `git revert <id_commit>` | Crea un nuevo commit que deshace uno anterior | `git revert a1b2c3d` |
| `git stash` | Guarda temporalmente los cambios sin hacer commit | `git stash` |
| `git stash pop` | Restaura los cambios guardados en el stash | `git stash pop` |
| `git rm <archivo>` | Elimina un archivo del repositorio y del sistema | `git rm data.csv` |
| `git mv <antiguo> <nuevo>` | Cambia el nombre o mueve un archivo | `git mv viejo.txt nuevo.txt` |
| `git tag <nombre>` | Crea una etiqueta (tag) en el commit actual | `git tag v1.0.0` |
| `git tag -a <nombre> -m "<mensaje>"` | Crea una etiqueta anotada | `git tag -a v1.0.0 -m "Versión inicial"` |
| `git push origin --tags` | Envía las etiquetas al remoto | `git push origin --tags` |
| `git show <id_commit>` | Muestra los detalles de un commit específico | `git show a1b2c3d` |
| `git blame <archivo>` | Muestra quién modificó cada línea de un archivo | `git blame main.py` |
| `git clean -f` | Elimina archivos no rastreados (untracked) | `git clean -f` |
| `git reflog` | Muestra el historial de movimientos (commits, resets, checkouts) | `git reflog` |
| `git cherry-pick <id_commit>` | Aplica un commit específico en la rama actual | `git cherry-pick a1b2c3d` |
| `git merge --abort` | Cancela una fusión en conflicto | `git merge --abort` |
| `git rebase <rama>` | Reorganiza commits encima de otra rama | `git rebase main` |
| `git rebase --continue` | Continúa un rebase tras resolver conflictos | `git rebase --continue` |
| `git remote remove <nombre>` | Elimina un repositorio remoto | `git remote remove origin` |
| `git config --global core.editor "code --wait"` | Configura VSCode como editor de Git | `git config --global core.editor "code --wait"` |
| `git shortlog -sn` | Muestra una lista de contribuyentes ordenada por cantidad de commits | `git shortlog -sn` |
| `git archive --format=zip HEAD -o proyecto.zip` | Crea un ZIP del proyecto actual | `git archive --format=zip HEAD -o proyecto.zip` |

---

