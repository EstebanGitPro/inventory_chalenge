from data.utils import obtener_ruta_absoluta
import csv


def leer_todas_solicitudes():
    ruta_csv = obtener_ruta_absoluta('data/solicitudes.csv')
    
    if not ruta_csv:
        return None, None
    
    solicitudes = []
    fieldnames = None
    
    with open(ruta_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        fieldnames = lector.fieldnames
        for fila in lector:
            solicitudes.append(fila)
    
    return solicitudes, fieldnames


def buscar_solicitudes_pendientes():
    solicitudes, _ = leer_todas_solicitudes()
    
    if not solicitudes:
        return []
    
    pendientes = [s for s in solicitudes if s['estado'].lower() == 'pendiente']
    return pendientes
