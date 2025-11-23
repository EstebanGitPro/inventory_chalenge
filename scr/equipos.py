
from data.writers import registrar_equipo
from data.utils import id
from datetime import datetime

print("=="*30)
print("AGREGAR EQUIPO")
print("=="*30)


date = datetime.now()





equipo_id = id()
nombre_equipo = input("Por favor, ingresa el nombre del equipo: ")
categoria = input("Por favor, ingresa la categoria del equipo: ")
estado_actual = input("Por favor, ingresa el estado actual del equipo: ")
fecha_registro = date.strftime("%Y-%m-%d")
descripcion = input("Por favor, una descripcion del equipo(opcional): ") 



def agregar_equipo(equipo_id, nombre_equipo, categoria , estado_actual, fecha_registro, descripcion="N/A" ):
    resultado = registrar_equipo(equipo_id, nombre_equipo, categoria , estado_actual, fecha_registro, descripcion )
    if resultado:
        print("Equipo agregado exitosamente")
    else:
        print("Hubo un error al agregar el equipo")
    
    
    
    
agregar_equipo(equipo_id, nombre_equipo, categoria , estado_actual, fecha_registro, descripcion)
