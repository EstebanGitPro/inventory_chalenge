from data.utils import obtener_ruta_absoluta
from data.readers import cargar_csv_completo
import csv


def registrar_prestamo(equipo_id, nombre, tipo_usuario, fecha_prestamo, fecha_devolucion, dias_prestamo, estado='activo'):
    ruta_csv = obtener_ruta_absoluta('data/prestamos.csv')
    
    datos = {
        "equipo_id": equipo_id,
        "nombre": nombre,
        "tipo_usuario": tipo_usuario,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "dias_prestamo": dias_prestamo,
        "estado": estado
    }
        
    if ruta_csv:
        with open(ruta_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['equipo_id', 'nombre', 'tipo_usuario', 'fecha_prestamo', 'fecha_devolucion', 'dias_prestamo', 'estado'])
            if cargar_csv_completo('data/prestamos.csv') == []:
                escritor.writeheader()
                escritor.writerow(datos)
            else:
                escritor.writerow(datos)
        return True
    return False


def sobrescribir_prestamos(prestamos, fieldnames):
    ruta_csv = obtener_ruta_absoluta('data/prestamos.csv')
    
    if not ruta_csv:
        return False
    
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(prestamos)
    
    return True
