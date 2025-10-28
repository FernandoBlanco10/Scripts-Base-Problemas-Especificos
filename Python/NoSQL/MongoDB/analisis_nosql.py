# Script: Analisis de la coleccion 'usuarios' y almacenamiento de resultados en 'analisis_usuarios'

from pymongo import MongoClient
import json
from datetime import datetime

# --- Conectar a MongoDB ---
client = MongoClient(GetVar('client'))
db = client[GetVar('db')]
usuarios_col = db["usuarios"]         
analisis_col = db["analisis_usuarios"] 

# --- Fecha de análisis ---
fecha_analisis = datetime.now().isoformat()

# --- Total de registros ---
total_registros = usuarios_col.count_documents({})
print(total_registros)

# --- Conteo de registros por Ciudad ---
pipeline_ciudad = [
    {"$group": {"_id": "$Ciudad", "cantidad": {"$sum": 1}}},
    {"$sort": {"cantidad": -1}}
]
registros_por_ciudad = list(usuarios_col.aggregate(pipeline_ciudad))

# --- Conteo de registros por Tipo_Pago ---
pipeline_pago = [
    {"$group": {"_id": "$Tipo_Pago", "cantidad": {"$sum": 1}}},
    {"$sort": {"cantidad": -1}}
]
registros_por_pago = list(usuarios_col.aggregate(pipeline_pago))

# --- Ventas totales por Producto ---
pipeline_ventas_producto = [
    {"$group": {"_id": "$Producto", "total_ventas": {"$sum": "$Total"}}},
    {"$sort": {"total_ventas": -1}}
]
ventas_por_producto = list(usuarios_col.aggregate(pipeline_ventas_producto))

# --- Ciudad con mayor venta total ---
pipeline_ciudad_top_venta = [
    {"$group": {"_id": "$Ciudad", "ventas_totales": {"$sum": "$Total"}}},
    {"$sort": {"ventas_totales": -1}},
    {"$limit": 1}
]
ciudad_top_venta = list(usuarios_col.aggregate(pipeline_ciudad_top_venta))
ciudad_top = ciudad_top_venta[0]["_id"] if ciudad_top_venta else None
ventas_top = ciudad_top_venta[0]["ventas_totales"] if ciudad_top_venta else 0

# --- Crear documento de análisis ---
analisis = {
    "fecha_analisis": fecha_analisis,
    "total_registros": total_registros,
    "registros_por_ciudad": registros_por_ciudad,
    "registros_por_pago": registros_por_pago,
    "ventas_por_producto": ventas_por_producto,
    "ciudad_mas_ventas": ciudad_top,
    "total_ventas_ciudad_top": ventas_top
}

# --- Insertar en la colección de análisis ---
result = analisis_col.insert_one(analisis)
print(f"Documento de análisis insertado con ID: {result.inserted_id}")

SetVar('ciudad_mas_ventas',ciudad_top)

# --- Cerrar conexión ---
client.close()
