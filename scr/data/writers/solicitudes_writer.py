from data.utils import obtener_ruta_absoluta
from data.readers import cargar_csv_completo
import csv


def registro_solicitud(equipo_id, nombre, tipo_usuario, fecha_prestamo, dias_prestamo, estado='pendiente'):
    ruta_csv = obtener_ruta_absoluta('data/solicitudes.csv')
    
    datos = {
        "equipo_id": equipo_id,
        "nombre": nombre,
        "tipo_usuario": tipo_usuario,
        "fecha_prestamo": fecha_prestamo,
        "dias_prestamo": dias_prestamo,
        "estado": estado
    }
        
    if ruta_csv:
        with open(ruta_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['equipo_id', 'nombre', 'tipo_usuario', 'fecha_prestamo', 'dias_prestamo', 'estado'])
            if cargar_csv_completo('data/solicitudes.csv') == []:
                escritor.writeheader()
                escritor.writerow(datos)
            else:
                escritor.writerow(datos)
        return True
    return False