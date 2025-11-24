from data.utils import obtener_ruta_absoluta
from data.readers import cargar_csv_completo
import csv
from datetime import datetime

def registrar_historial_equipo(equipo_id, nombre_equipo, fecha_prestamo, fecha_devolucion, usuario, estado):
    ruta_csv = obtener_ruta_absoluta('data/historial_equpos.csv')
    
    datos = {
        "equipo_id": equipo_id,
        "nombre_equipo": nombre_equipo,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "usuario": usuario,
        "estado": estado,
        "fecha_registro": datetime.now().strftime("%d/%m/%Y")
    }
    
    if ruta_csv:
        with open(ruta_csv, 'a', newline='', encoding='utf-8') as archivo:
            fieldnames = ['equipo_id', 'nombre_equipo', 'fecha_prestamo', 'fecha_devolucion', 'usuario', 'estado', 'fecha_registro']
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
            if cargar_csv_completo('data/historial_equpos.csv') == []:
                escritor.writeheader()
            escritor.writerow(datos)
        return True
    return False

def registrar_historial_usuario(usuario, tipo_usuario, equipo_id, nombre_equipo, fecha_prestamo, fecha_devolucion, retraso):
    ruta_csv = obtener_ruta_absoluta('data/historial_usuarios.csv')
    
    datos = {
        "usuario": usuario,
        "tipo_usuario": tipo_usuario,
        "equipo_id": equipo_id,
        "nombre_equipo": nombre_equipo,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "retraso": retraso,
        "fecha_registro": datetime.now().strftime("%d/%m/%Y")
    }
    
    if ruta_csv:
        with open(ruta_csv, 'a', newline='', encoding='utf-8') as archivo:
            fieldnames = ['usuario', 'tipo_usuario', 'equipo_id', 'nombre_equipo', 'fecha_prestamo', 'fecha_devolucion', 'retraso', 'fecha_registro']
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
            if cargar_csv_completo('data/historial_usuarios.csv') == []:
                escritor.writeheader()
            escritor.writerow(datos)
        return True
    return False
