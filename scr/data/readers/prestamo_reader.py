from data.utils import obtener_ruta_absoluta
import csv


def leer_todos_prestamos():
    ruta_csv = obtener_ruta_absoluta('data/prestamos.csv')
    
    if not ruta_csv:
        return None, None
    
    prestamos = []
    fieldnames = None
    
    with open(ruta_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        fieldnames = lector.fieldnames
        for fila in lector:
            prestamos.append(fila)
    
    return prestamos, fieldnames


def buscar_prestamos_activos():
    prestamos, _ = leer_todos_prestamos()
    
    if not prestamos:
        return []
    
    activos = [p for p in prestamos if p['estado'].lower() == 'activo']
    return activos


def buscar_prestamo_equipo(equipo_id):
    prestamos, _ = leer_todos_prestamos()
    
    if not prestamos:
        return None
    
    for prestamo in prestamos:
        if prestamo['equipo_id'] == equipo_id and prestamo['estado'].lower() == 'activo':
            return prestamo
    
    return None
