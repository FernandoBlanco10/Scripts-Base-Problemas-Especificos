# Script: Registro de ejecución de un bot en MongoDB
# Este script crea un documento en la colección especificada para almacenar
# la información de inicio de ejecución de un bot, incluyendo fecha, estado
# y duración de la ejecución (inicialmente nula).

import json
from datetime import datetime
from pymongo import MongoClient

# --- Variables de entrada ---
bot_name = GetVar('bot_name')          # bot_name = "Bitacora_NoSQL"

# --- Fecha y hora de inicio de la ejecución ---
inicio = datetime.now().isoformat()

# --- Estado inicial de la ejecución ---
estado = "Iniciando"

# --- Conexión a MongoDB ---
# Se obtienen los parámetros de conexión desde Rocketbot
client = MongoClient(GetVar('client'))  # "client = mongodb://localhost:27017/"
db = client[GetVar('db')]               # db = "miBaseDeDatos"
collection = db[GetVar('collection')]   # collection = "bitacora"

# --- Creación del documento de ejecución ---
# Se construye un diccionario con los campos que se almacenarán en MongoDB
ejecucion = {
    "bot_name": bot_name,         
    "inicio": inicio,             
    "fin": None,                  
    "estado": estado,             
    "archivo_encontrado": None,   
    "duracion_segundos": None     
}

# --- Inserción del documento en la colección ---
result = collection.insert_one(ejecucion)
doc_id = result.inserted_id  # Guardar el ID generado por MongoDB

# --- Cierre de la conexión ---
client.close()

# --- Variables de salida para Rocketbot ---
SetVar('doc_id', doc_id)  # Se guarda el ID del documento insertado para su seguimiento
