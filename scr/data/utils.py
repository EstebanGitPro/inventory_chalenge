import os
import uuid
from datetime import datetime
def obtener_ruta_absoluta(ruta_relativa):
    """
    Convierte una ruta relativa al directorio scr/ en una ruta absoluta.
    
    Args:
        ruta_relativa (str): Ruta relativa desde el directorio scr/
        
    Returns:
        str: Ruta absoluta al archivo
        
    Ejemplo:
        obtener_ruta_absoluta('data/usuario_admin.csv')
        -> '/Users/estebandev/Documents/python/inventory_chalenge/scr/data/usuario_admin.csv'
    """
    if os.path.isabs(ruta_relativa):
        return ruta_relativa
    
    # Obtener el directorio del script actual
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    # Subir un nivel hasta scr/
    dir_scr = os.path.dirname(dir_actual)
    # Construir la ruta completa
    return os.path.join(dir_scr, ruta_relativa)


def id():
    uuid_unico = str(uuid.uuid4())
    return uuid_unico


def iguala_formato(string):
    formatos_soportados = [
        {
            "formato": "%d/%m/%Y",
            "ejemplo": "11/05/2022"},
        {
            "formato": "%Y-%m-%d", 
            "ejemplo": "2022-05-11"}
    ]
    
    mi_formato = "%d/%m/%Y"
    for formato in formatos_soportados:
        try:
            dt = datetime.strptime(string, formato["formato"])
            return dt.strftime(mi_formato)
        except ValueError:
            continue
    return None





    
 




