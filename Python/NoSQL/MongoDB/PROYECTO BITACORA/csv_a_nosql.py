# Script: CSV a MongoDB
# Descripción: Carga registros de un CSV a una colección de MongoDB y guarda estadísticas de la operación.

import pandas as pd
from pymongo import MongoClient
import json

ruta = GetVar('_ruta_csv')

# Conectarse a MongoDB y seleccionar base de datos y colección
client = MongoClient("mongodb://localhost:27017/")
db = client["miBaseDeDatos"]
collection = db["usuarios"]

# Leer el CSV con pandas, usando codificación UTF-8
df = pd.read_csv(ruta, encoding='utf-8')
registros_leidos = df.count()

# Convertir DataFrame a una lista de diccionarios, formato requerido por MongoDB
data = json.loads(df.to_json(orient='records'))

# Insertar registros en MongoDB si existen
if data:
    result = collection.insert_many(data)
    print(f"{len(result.inserted_ids)} documentos insertados correctamente.")

# Contar todos los documentos actuales en la colección
registros_cargados = collection.count_documents()

client.close()

SetVar('registros_leidos', registros_leidos)
SetVar('registros_cargados', registros_cargados)
