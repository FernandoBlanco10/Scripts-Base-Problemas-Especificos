# 📁 Proyecto: Registro y Análisis de Ejecuciones con MongoDB

## 🧩 Descripción General
Este proyecto está compuesto por un conjunto de **scripts en Python** diseñados para **gestionar, registrar y analizar la ejecución de procesos automatizados (robots)** utilizando una base de datos **NoSQL en MongoDB**.  
El objetivo es mantener una **bitácora centralizada y estructurada** de los procesos ejecutados, su estado, duración, y datos relevantes para su análisis posterior.

---

## 🧠 Objetivo del Proyecto
Proporcionar una solución modular que permita:
- Registrar el inicio y fin de ejecución de cada robot.
- Guardar y transformar datos desde archivos `.csv` a una base de datos NoSQL.
- Analizar los datos almacenados mediante consultas o el framework de agregación de MongoDB.
- Mantener trazabilidad y control de los procesos automatizados.

---

## 📂 Estructura de la Carpeta

| Archivo | Descripción |
|----------|--------------|
| **`inicio_robot_bitacora.py`** | Registra el **inicio** de un robot en la bitácora, guardando la hora, el nombre del proceso y su identificador. |
| **`csv_a_nosql.py`** | Convierte datos de un archivo `.csv` a **documentos JSON** y los inserta en una colección de MongoDB para su almacenamiento y consulta. |
| **`analisis_nosql.py`** | Ejecuta **consultas y análisis** sobre los datos en MongoDB, aprovechando el framework de agregación para generar reportes o métricas. |
| **`fin_robot_bitacora.py`** | Actualiza el **estado final** del robot en la bitácora (éxito o falla), calcula la duración de ejecución y marca la hora de finalización. |

---

## ⚙️ Flujo General del Sistema

1. **Inicio de ejecución:**  
   El script `inicio_robot_bitacora.py` crea un nuevo registro en MongoDB con los datos básicos del robot (fecha, hora, nombre y estado inicial).

2. **Procesamiento de datos:**  
   El script `csv_a_nosql.py` puede ejecutarse para migrar información de archivos CSV a la base de datos, facilitando el acceso a datos estructurados y no estructurados.

3. **Finalización del robot:**  
   Al concluir el proceso, `fin_robot_bitacora.py` actualiza el registro con la hora de fin, duración total y estado final (`OK` o `FALLA`).

4. **Análisis posterior:**  
   Finalmente, `analisis_nosql.py` permite ejecutar consultas y generar reportes que ayudan a identificar patrones, fallas recurrentes o métricas de desempeño.

---

## 🧾 Ejemplo de Documento en la Bitácora

```json
{
  "_id": "671e38d7bfa2c33412ab3456",
  "robot": "CargaUsuarios",
  "inicio": "2025-10-28T09:30:00",
  "fin": "2025-10-28T09:34:15",
  "duracion_segundos": 255,
  "archivo_encontrado": "usuarios.csv",
  "estado": "OK"
}
