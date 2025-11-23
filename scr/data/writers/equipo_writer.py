import csv
from data.utils import obtener_ruta_absoluta
from data.readers import cargar_csv_completo



def registrar_equipo(equipo_id, nombre_equipo, categoria , estado_actual, fecha_registro, descripcion ):

    ruta_csv = obtener_ruta_absoluta('data/equipos.csv')    
    if ruta_csv:
        
            with open(ruta_csv, 'a', newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=['equipo_id', 'nombre_equipo', 'categoria', 'estado_actual', 'fecha_registro', 'descripcion'])
                if  cargar_csv_completo('data/equipos.csv') == []:
                    escritor.writeheader()
                    escritor.writerow({'equipo_id': equipo_id, 'nombre_equipo': nombre_equipo, 'categoria': categoria, 'estado_actual': estado_actual, 'fecha_registro': fecha_registro, 'descripcion': descripcion})
                else:
                    escritor.writerow({'equipo_id': equipo_id, 'nombre_equipo': nombre_equipo, 'categoria': categoria, 'estado_actual': estado_actual, 'fecha_registro': fecha_registro, 'descripcion': descripcion})
                return True
    return False

