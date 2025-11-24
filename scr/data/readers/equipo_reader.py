from data.utils import obtener_ruta_absoluta
import csv

def buscar_equipo(equipo_id,estado_actual):
    ruta_csv = obtener_ruta_absoluta('data/equipos.csv')
    
    with open(ruta_csv, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)  
        for fila in lector:
            if fila['equipo_id'] == equipo_id:
                return fila
    return False

