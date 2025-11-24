from data.writers import registrar_equipo, sobrescribir_equipos
from data.readers import leer_todos_equipos
from data.utils import id
from datetime import datetime


def agregar_equipo(equipo_id, nombre_equipo, categoria, estado_actual, fecha_registro, descripcion="N/A"):
    resultado = registrar_equipo(equipo_id, nombre_equipo, categoria, estado_actual, fecha_registro, descripcion)
    if resultado:
        print("Equipo agregado exitosamente")
    else:
        print("Hubo un error al agregar el equipo")


def actualizar_estado_equipo(equipo_id, nuevo_estado):
    equipos, fieldnames = leer_todos_equipos()
    
    if equipos is None:
        return False
    
    equipo_encontrado = False
    
    for equipo in equipos:
        if equipo['equipo_id'] == equipo_id:
            equipo['estado_actual'] = nuevo_estado
            equipo_encontrado = True
            break
    
    if not equipo_encontrado:
        return False
    
    return sobrescribir_equipos(equipos, fieldnames)
