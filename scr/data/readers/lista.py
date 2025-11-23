import csv
from data.utils import obtener_ruta_absoluta


def cargar_csv_completo(ruta_archivo):
    """
    Carga todos los datos de un archivo CSV.
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV (relativa a scr/ o absoluta)
        
    Returns:
        list: Lista de diccionarios con los datos del CSV
    """
    datos = []
    ruta_absoluta = obtener_ruta_absoluta(ruta_archivo)
    
    try:
        with open(ruta_absoluta, 'r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                datos.append(fila)
    except FileNotFoundError:
        print(f"Archivo {ruta_absoluta} no encontrado. Se creará al guardar datos.")
    
    return datos