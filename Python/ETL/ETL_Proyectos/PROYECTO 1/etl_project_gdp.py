# -----------------------------------------------------------------------------
# Código ETL para procesar información sobre el PIB de países
# -----------------------------------------------------------------------------
# Este script implementa un proceso ETL (Extracción, Transformación y Carga)
# que obtiene datos de un sitio web con información sobre el Producto Interno
# Bruto (PIB) nominal de distintos países, los transforma y los almacena tanto
# en un archivo CSV como en una base de datos SQLite.
#
# Autor: Fernando Blanco
# Fecha: 2025-10-30
# -----------------------------------------------------------------------------

# Importación de librerías necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime


# -----------------------------------------------------------------------------
# Función: extract
# -----------------------------------------------------------------------------
def extract(url, table_attribs):
    """
    Extrae información sobre países y su PIB desde una página web y la almacena
    en un DataFrame de pandas.

    La función realiza una solicitud HTTP al sitio web, analiza el contenido HTML
    utilizando BeautifulSoup, y filtra los datos correspondientes a los países
    y su PIB nominal en millones de USD.

    Args:
        url (str): URL de la página web a extraer.
        table_attribs (list): Lista con los nombres de las columnas del DataFrame.

    Returns:
        pd.DataFrame: DataFrame con la información extraída (país y PIB en millones de USD).
    """
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)

    # Localiza las tablas dentro del HTML y selecciona la correspondiente al PIB
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')

    # Recorre las filas y extrae los valores relevantes
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {
                    "Country": col[0].a.contents[0],
                    "GDP_USD_millions": col[2].contents[0]
                }
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)

    return df


# -----------------------------------------------------------------------------
# Función: transform
# -----------------------------------------------------------------------------
def transform(df):
    """
    Transforma la columna del PIB de millones a miles de millones (billones) de USD
    y la convierte de texto con formato de moneda a un valor numérico tipo float.

    También realiza el redondeo a dos decimales.

    Args:
        df (pd.DataFrame): DataFrame con la información original del PIB.

    Returns:
        pd.DataFrame: DataFrame con la columna del PIB transformada a billones.
    """
    GDP_list = df["GDP_USD_millions"].tolist()
    GDP_list = [float("".join(x.split(','))) for x in GDP_list]
    GDP_list = [np.round(x / 1000, 2) for x in GDP_list]
    df["GDP_USD_millions"] = GDP_list
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})
    return df


# -----------------------------------------------------------------------------
# Función: load_to_csv
# -----------------------------------------------------------------------------
def load_to_csv(df, csv_path):
    """
    Guarda el DataFrame final como un archivo CSV en la ruta especificada.

    Args:
        df (pd.DataFrame): DataFrame transformado a guardar.
        csv_path (str): Ruta del archivo CSV destino.
    """
    df.to_csv(csv_path, index=False)


# -----------------------------------------------------------------------------
# Función: load_to_db
# -----------------------------------------------------------------------------
def load_to_db(df, sql_connection, table_name):
    """
    Carga el DataFrame final a una tabla en una base de datos SQLite.

    Si la tabla ya existe, será reemplazada.

    Args:
        df (pd.DataFrame): DataFrame a almacenar.
        sql_connection (sqlite3.Connection): Conexión activa a la base de datos SQLite.
        table_name (str): Nombre de la tabla destino.
    """
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)


# -----------------------------------------------------------------------------
# Función: run_query
# -----------------------------------------------------------------------------
def run_query(query_statement, sql_connection):
    """
    Ejecuta una sentencia SQL sobre la base de datos y muestra los resultados
    en la consola.

    Args:
        query_statement (str): Consulta SQL a ejecutar.
        sql_connection (sqlite3.Connection): Conexión a la base de datos SQLite.
    """
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


# -----------------------------------------------------------------------------
# Función: log_progress
# -----------------------------------------------------------------------------
def log_progress(message):
    """
    Registra en un archivo de log un mensaje con marca temporal (timestamp).

    Args:
        message (str): Mensaje descriptivo del progreso o estado del proceso.
    """
    timestamp_format = '%Y-%m-%d-%H:%M:%S'  # Formato: Año-Mes-Día-Hora-Minuto-Segundo
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:
        f.write(f"{timestamp} : {message}\n")


# -----------------------------------------------------------------------------
# Ejecución del Proceso ETL
# -----------------------------------------------------------------------------
# A continuación se definen los parámetros de entrada y se ejecutan las fases
# del proceso ETL en orden: extracción, transformación, carga y consulta.

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'

log_progress('Configuración inicial completada. Iniciando proceso ETL.')

# Fase de extracción
df = extract(url, table_attribs)
log_progress('Extracción de datos completada. Iniciando transformación.')

# Fase de transformación
df = transform(df)
log_progress('Transformación de datos completada. Iniciando carga.')

# Fase de carga a CSV
load_to_csv(df, csv_path)
log_progress('Datos almacenados en archivo CSV.')

# Fase de carga a base de datos SQLite
sql_connection = sqlite3.connect(db_name)
log_progress('Conexión con base de datos SQLite establecida.')

load_to_db(df, sql_connection, table_name)
log_progress('Datos cargados en base de datos. Ejecutando consulta de validación.')

# Ejecución de una consulta de verificación
query_statement = f"SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement, sql_connection)
log_progress('Proceso ETL completado correctamente.')

sql_connection.close()
