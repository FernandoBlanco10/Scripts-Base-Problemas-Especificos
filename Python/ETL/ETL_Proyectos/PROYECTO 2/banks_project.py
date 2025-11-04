# -----------------------------------------------------------------------------
# Código ETL para procesar información sobre los bancos más grandes del mundo
# -----------------------------------------------------------------------------
# Este script implementa un proceso ETL (Extracción, Transformación y Carga)
# que obtiene datos de un sitio web con información sobre los bancos con mayor
# capitalización de mercado, los transforma agregando conversiones de moneda
# a distintas divisas, y finalmente los almacena tanto en un archivo CSV como
# en una base de datos SQLite para su posterior consulta.
#
# Autor: Fernando Blanco
# Fecha: 2025-11-03
# -----------------------------------------------------------------------------

# Importación de librerías necesarias
from datetime import datetime
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3


# -----------------------------------------------------------------------------
# Función: log_progress
# -----------------------------------------------------------------------------
def log_progress(message):
    """
    Registra en un archivo de log un mensaje con marca temporal (timestamp).

    Args:
        message (str): Mensaje descriptivo del progreso o estado del proceso.
    """
    timestamp_format = "%Y-%m-%d-%H:%M:%S"  # Formato: Año-Mes-Día-Hora-Minuto-Segundo
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('code_log.txt', "a") as f:
        f.write(f"{timestamp} : {message}\n")


# -----------------------------------------------------------------------------
# Función: extract
# -----------------------------------------------------------------------------
def extract(url, table_attribs):
    """
    Extrae información sobre los bancos más grandes a partir de su
    capitalización de mercado desde una página web y la almacena en un DataFrame.

    La función utiliza BeautifulSoup para analizar el HTML de la página,
    localiza la tabla correspondiente y limpia los valores de capitalización
    de mercado, convirtiéndolos a formato numérico (float).

    Args:
        url (str): URL de la página web a extraer.
        table_attribs (list): Lista con los nombres de las columnas del DataFrame.

    Returns:
        pd.DataFrame: DataFrame con los nombres de los bancos y su capitalización
        de mercado en miles de millones de USD.
    """
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # Localiza el encabezado de la sección y la tabla asociada
    header = soup.find('span', {'id': 'By_market_capitalization'})
    h2 = header.find_parent('h2')
    table = h2.find_next('table')

    # Convierte la tabla HTML en un DataFrame
    df = pd.read_html(str(table))[0]

    # Identifica la columna de capitalización de mercado (nombre varía por formato)
    col_name = [c for c in df.columns if 'Market cap' in c or 'Market Cap' in c][0]

    # Limpieza y conversión de la columna a tipo numérico
    df[col_name] = (
        df[col_name]
        .astype(str)
        .str.replace(',', '')  # Elimina comas de miles
        .str.strip()
        .astype(float)
    )

    # Renombra la columna para estandarizarla
    df.rename(columns={col_name: 'MC_USD_Billion'}, inplace=True)

    return df


# -----------------------------------------------------------------------------
# Función: transform
# -----------------------------------------------------------------------------
def transform(df, csv_path):
    """
    Transforma los datos agregando conversiones de capitalización de mercado
    (Market Cap) a otras divisas utilizando tasas de cambio desde un archivo CSV.

    El archivo CSV debe contener las columnas:
    - 'Currency': Nombre de la divisa.
    - 'Rate': Tasa de conversión respecto al dólar (USD).

    Se añaden tres columnas al DataFrame:
    - MC_GBP_Billion
    - MC_EUR_Billion
    - MC_INR_Billion

    Args:
        df (pd.DataFrame): DataFrame con la información original.
        csv_path (str): Ruta al archivo CSV con las tasas de cambio.

    Returns:
        pd.DataFrame: DataFrame con las columnas de conversión agregadas.
    """
    dataframe = pd.read_csv(csv_path)
    dict_rates = dataframe.set_index('Currency').to_dict()['Rate']

    # Cálculo de conversiones y redondeo a dos decimales
    df['MC_GBP_Billion'] = [np.round(x * dict_rates['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * dict_rates['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * dict_rates['INR'], 2) for x in df['MC_USD_Billion']]

    return df


# -----------------------------------------------------------------------------
# Función: load_to_csv
# -----------------------------------------------------------------------------
def load_to_csv(df, output_path):
    """
    Guarda el DataFrame final como un archivo CSV en la ruta especificada.

    Args:
        df (pd.DataFrame): DataFrame transformado a guardar.
        output_path (str): Ruta del archivo CSV destino.
    """
    df.to_csv(output_path, index=False)


# -----------------------------------------------------------------------------
# Función: load_to_db
# -----------------------------------------------------------------------------
def load_to_db(df, sql_connection, table_name):
    """
    Carga el DataFrame final en una tabla dentro de una base de datos SQLite.

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
    print("\n" + query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


# -----------------------------------------------------------------------------
# Ejecución del Proceso ETL
# -----------------------------------------------------------------------------
# A continuación se definen los parámetros de entrada y se ejecutan las fases
# del proceso ETL en orden: extracción, transformación, carga y consulta.

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = ['Bank name', 'MC_USD_Billion']
csv_path = 'exchange_rate.csv'
output_path = './Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'

log_progress('Configuración inicial completada. Iniciando proceso ETL.')

# Fase de extracción
df = extract(url, table_attribs)
log_progress('Extracción de datos completada. Iniciando transformación.')

# Fase de transformación
df = transform(df, csv_path)
log_progress('Transformación de datos completada. Iniciando carga.')

# Fase de carga a CSV
load_to_csv(df, output_path)
log_progress('Datos almacenados en archivo CSV.')

# Fase de carga a base de datos SQLite
sql_connection = sqlite3.connect(db_name)
log_progress('Conexión con base de datos SQLite establecida.')

load_to_db(df, sql_connection, table_name)
log_progress('Datos cargados en base de datos. Ejecutando consultas de validación.')

# Ejecución de consultas de verificación
query_statement = f"SELECT * FROM {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT [Bank Name] FROM {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress('Proceso ETL completado correctamente.')

# Cierre de la conexión con la base de datos
sql_connection.close()
log_progress('Conexión con la base de datos cerrada correctamente.')
