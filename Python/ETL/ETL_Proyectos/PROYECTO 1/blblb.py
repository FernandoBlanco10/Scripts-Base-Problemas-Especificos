# ----------------------------------------------------------------------------- 
# Extracción de la tabla "By market capitalization" de Wikipedia
# ----------------------------------------------------------------------------- 
from bs4 import BeautifulSoup
import requests
import pandas as pd

# ----------------------------------------------------------------------------- 
# Función: extract
# ----------------------------------------------------------------------------- 
def extract(url, table_attribs):
    """
    Extrae información de los bancos por capitalización de mercado desde la página web
    de Wikipedia y la devuelve como un DataFrame de pandas.

    Args:
        url (str): URL de la página web.
        table_attribs (list): Lista con los nombres de las columnas del DataFrame.

    Returns:
        pd.DataFrame: DataFrame con Rank, Bank name y Market Cap en miles de millones de USD.
    """
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # 1. Buscar el encabezado "By market capitalization"
    header = soup.find('span', {'id': 'By_market_capitalization'})
    if not header:
        raise ValueError("No se encontró el encabezado 'By market capitalization'")

    # 2. Encontrar el <h2> padre y luego la primera tabla que aparece después
    h2 = header.find_parent('h2')
    table = h2.find_next('table')  # toma la primera tabla que aparezca después

    if not table:
        raise ValueError("No se encontró la tabla después del encabezado")

    # 3. Convertir tabla a DataFrame
    df = pd.read_html(str(table))[0]

    # 4. Limpiar la columna de Market Cap
    # Buscar columna que contenga 'Market cap' en el nombre
    col_name = [c for c in df.columns if 'Market cap' in c or 'Market Cap' in c][0]
    df[col_name] = (
        df[col_name]
        .astype(str)
        .str.replace(',', '')  # eliminar separadores de miles
        .str.strip()           # eliminar espacios y saltos de línea
        .astype(float)
    )

    # 5. Renombrar columna
    df.rename(columns={col_name: 'MC_USD_Billion'}, inplace=True)

    # 6. Seleccionar solo las columnas requeridas (si table_attribs se pasó)
    if table_attribs:
        df = df[table_attribs]

    return df

# ----------------------------------------------------------------------------- 
# Llamada de ejemplo
# ----------------------------------------------------------------------------- 
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Rank', 'Bank name', 'MC_USD_Billion']

df_banks = extract(url, table_attribs)
print(df_banks)
