from data.utils import obtener_ruta_absoluta
import csv


def buscar_equipo(equipo_id, estado_actual=None):
    ruta_csv = obtener_ruta_absoluta('data/equipos.csv')
    
    with open(ruta_csv, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)  
        for fila in lector:
            if fila['equipo_id'] == equipo_id:
                return fila
    return False


def leer_todos_equipos():
    ruta_csv = obtener_ruta_absoluta('data/equipos.csv')
    
    if not ruta_csv:
        return None, None
    
    equipos = []
    fieldnames = None
    
    with open(ruta_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        fieldnames = lector.fieldnames
        for fila in lector:
            equipos.append(fila)
    
    return equipos, fieldnames
