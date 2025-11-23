import csv
from data.utils import obtener_ruta_absoluta
from data.readers import cargar_csv_completo


def registro_usuario_admin(nombre: str, contrasena: str, rol: str):
    ruta_csv = obtener_ruta_absoluta('data/usuario_admin.csv')
    if ruta_csv:
        with open(ruta_csv, 'w', newline='') as archivo:
                 escritor = csv.DictWriter(archivo, fieldnames=['usuario', 'contrasena', 'rol'])
                 escritor.writeheader()
                 escritor.writerow({'usuario': nombre, 'contrasena': contrasena, 'rol': rol})
                 return True
    else:
        print("Error: No se pudo escribir el archivo")
        return False


