import csv
from data.utils import obtener_ruta_absoluta


def buscar_usuario_admin(nombre):
    """
    Busca un usuario administrador por nombre.
    
    Args:
        nombre (str): Nombre del usuario a buscar
        
    Returns:
        dict | None: Diccionario con datos del usuario o None si no existe
    """
    ruta_csv = obtener_ruta_absoluta('data/usuario_admin.csv')
    
    with open(ruta_csv, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)  
        for fila in lector:
            if fila['usuario'] == nombre:
                return fila
    return None


def login_usuario_admin(nombre, contrasena):
    
    if nombre == "" or contrasena == "":
        return print("Error: El nombre o la contraseña no validos")
    
    usuario = buscar_usuario_admin(nombre)
    
    if usuario and usuario['contrasena'] == contrasena:
        return usuario
    
    return print("Error: El nombre o la contraseña no validos")
