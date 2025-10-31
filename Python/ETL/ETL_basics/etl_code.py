"""
ETL Pipeline Script
===================

Este script implementa un proceso ETL (Extract, Transform, Load) completo,
capaz de integrar datos desde archivos CSV, JSON y XML en un único archivo 
transformado en formato CSV. 

El proceso incluye:
    1. Extracción de datos desde múltiples formatos.
    2. Transformación de unidades (altura y peso).
    3. Carga de datos en un archivo consolidado.
    4. Registro detallado de logs en cada fase del proceso.

Autor: Fernando Blanco
Fecha: 2025-10-30
Versión: 1.0
"""

import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuración Global
# ---------------------------------------------------------------------------

log_file = "log_file.txt"             # Archivo donde se registran logs del proceso
target_file = "transformed_data.csv"  # Archivo destino con los datos procesados


# ---------------------------------------------------------------------------
# Funciones de Extracción
# ---------------------------------------------------------------------------

def extract_from_csv(file_to_process: str) -> pd.DataFrame:
    """
    Extrae datos desde un archivo CSV y los carga en un DataFrame.

    Args:
        file_to_process (str): Ruta del archivo CSV a procesar.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos.
    """
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process: str) -> pd.DataFrame:
    """
    Extrae datos desde un archivo JSON (líneas múltiples) y los carga en un DataFrame.

    Args:
        file_to_process (str): Ruta del archivo JSON a procesar.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos.
    """
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process: str) -> pd.DataFrame:
    """
    Extrae datos desde un archivo XML y los carga en un DataFrame.

    Args:
        file_to_process (str): Ruta del archivo XML a procesar.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos del XML.
    """
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat(
            [dataframe, pd.DataFrame([{"name": name, "height": height, "weight": weight}])],
            ignore_index=True
        )

    return dataframe


def extract() -> pd.DataFrame:
    """
    Orquesta la fase de extracción combinando datos desde múltiples fuentes:
    CSV, JSON y XML.

    Returns:
        pd.DataFrame: DataFrame consolidado con todos los registros extraídos.
    """
    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

    # Procesar archivos CSV
    for csvfile in glob.glob("*.csv"):
        if csvfile != target_file:  # Evita procesar el archivo final como entrada
            extracted_data = pd.concat(
                [extracted_data, extract_from_csv(csvfile)],
                ignore_index=True
            )

    # Procesar archivos JSON
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat(
            [extracted_data, extract_from_json(jsonfile)],
            ignore_index=True
        )

    # Procesar archivos XML
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat(
            [extracted_data, extract_from_xml(xmlfile)],
            ignore_index=True
        )

    return extracted_data


# ---------------------------------------------------------------------------
# Función de Transformación
# ---------------------------------------------------------------------------

def transform(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformaciones a las columnas de altura y peso:
        - Convierte altura de pulgadas a metros.
        - Convierte peso de libras a kilogramos.

    Args:
        data (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame transformado.
    """
    data['height'] = (data['height'] * 0.0254).round(2)
    data['weight'] = (data['weight'] * 0.45359237).round(2)
    return data


# ---------------------------------------------------------------------------
# Función de Carga
# ---------------------------------------------------------------------------

def load_data(target_file: str, transformed_data: pd.DataFrame) -> None:
    """
    Carga los datos transformados en un archivo CSV.

    Args:
        target_file (str): Nombre del archivo de salida.
        transformed_data (pd.DataFrame): DataFrame a guardar.
    """
    transformed_data.to_csv(target_file, index=False)


# ---------------------------------------------------------------------------
# Función de Logging
# ---------------------------------------------------------------------------

def log_progress(message: str) -> None:
    """
    Registra un mensaje en el archivo de log con marca de tiempo.

    Args:
        message (str): Mensaje descriptivo del estado del proceso.
    """
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(f"{timestamp},{message}\n")


# ---------------------------------------------------------------------------
# Ejecución del Pipeline ETL
# ---------------------------------------------------------------------------

log_progress("Proceso ETL iniciando...")

log_progress("Fase de extracción iniciada")
extracted_data = extract()
log_progress("Fase de extracción terminada")

log_progress("Fase de transformación iniciada")
transformed_data = transform(extracted_data)
print("Datos transformados:\n", transformed_data)
log_progress("Fase de transformación terminada")

log_progress("Fase de carga iniciada")
load_data(target_file, transformed_data)
log_progress("Fase de carga terminada")

log_progress("Proceso ETL finalizado con éxito.")