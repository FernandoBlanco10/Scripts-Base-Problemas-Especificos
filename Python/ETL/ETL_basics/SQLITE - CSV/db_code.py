"""
Script: db_code.py
Autor: Fernando Blanco
Descripción:
    Este script implementa un proceso ETL (Extract, Transform, Load) simple
    utilizando SQLite y Pandas. Su objetivo es cargar datos desde un archivo CSV
    hacia una tabla en una base de datos SQLite, realizar consultas básicas 
    y demostrar cómo insertar nuevos registros programáticamente.
"""

import sqlite3
import pandas as pd

# -----------------------------------------------------------------------------
# 1. CONEXIÓN A LA BASE DE DATOS SQLITE
# -----------------------------------------------------------------------------
# Si la base de datos 'STAFF.db' no existe, SQLite la crea automáticamente.
conn = sqlite3.connect('STAFF.db')

# -----------------------------------------------------------------------------
# 2. DEFINICIÓN DE VARIABLES Y ESTRUCTURA DE LA TABLA
# -----------------------------------------------------------------------------
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# -----------------------------------------------------------------------------
# 3. EXTRACCIÓN DE DATOS DESDE CSV
# -----------------------------------------------------------------------------

file_path = "INSTRUCTOR.csv"

# Cargamos los datos del CSV en un DataFrame.
# 'names' asigna los encabezados de columna definidos manualmente.
df = pd.read_csv(file_path, names=attribute_list)

# -----------------------------------------------------------------------------
# 4. CARGA DE DATOS A SQLITE (ETL - LOAD)
# -----------------------------------------------------------------------------
# Si la tabla ya existe, será reemplazada completamente.
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Tabla creada o reemplazada exitosamente.')

# -----------------------------------------------------------------------------
# 5. CONSULTAS SQL BÁSICAS DESDE PANDAS
# -----------------------------------------------------------------------------

# a) Consultar todos los registros
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print("\nConsulta completa:\n", query_statement)
print(query_output)

# b) Consultar solo la columna FNAME
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print("\nConsulta de una columna:\n", query_statement)
print(query_output)

# c) Contar el número total de registros
query_statement = f"SELECT COUNT(*) AS total_registros FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print("\nConteo de registros:\n", query_statement)
print(query_output)

# -----------------------------------------------------------------------------
# 6. INSERCIÓN DE NUEVOS DATOS PROGRAMÁTICAMENTE
# -----------------------------------------------------------------------------
# Se crea un nuevo DataFrame con el registro a insertar.
data_dict = {
    'ID': [100],
    'FNAME': ['John'],
    'LNAME': ['Doe'],
    'CITY': ['Paris'],
    'CCODE': ['FR']
}
data_append = pd.DataFrame(data_dict)

# Agregamos el nuevo registro sin reemplazar la tabla.
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('\nNuevo registro agregado exitosamente.')

# -----------------------------------------------------------------------------
# 7. CIERRE DE CONEXIÓN
# -----------------------------------------------------------------------------
conn.close()
print('Conexión a la base de datos cerrada correctamente.')
