import json
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId 

# Obtener variables desde el entorno o desde Rocketbot
doc_id = GetVar('doc_id')                  # ID del documento de inicio en MongoDB
estatus_fin = GetVar('estatus_fin')        # Estado final de la ejecución ("True" o "False")

# Conexión a MongoDB
client = MongoClient(GetVar('client'))
db = client[GetVar('db')]
collection = db[GetVar('collection')]

# Conversión de ID a tipo ObjectId
doc_id = ObjectId(doc_id)

# Tiempos de ejecución
fin = datetime.now()                                   # Fecha y hora de finalización
ejecucion = collection.find_one({"_id": doc_id})       # Obtener el documento original
inicio = datetime.fromisoformat(ejecucion["inicio"])   # Parsear fecha de inicio
duracion = (fin - inicio).total_seconds()              # Calcular duración total (segundos)

# Actualizar documento según el resultado de la ejecución
if estatus_fin == "True":
    # Caso exitoso
    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "fin": fin.isoformat(),
            "duracion_segundos": duracion,
            "archivo_encontrado": archivo_encontrado,
            "estado": "OK"
        }}
    )
else:
    # Caso fallido
    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "fin": fin.isoformat(),
            "duracion_segundos": duracion,
            "estado": "FALLA"
        }}
    )

# Cerrar conexión
client.close()
