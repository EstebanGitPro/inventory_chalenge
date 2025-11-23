from data.readers import buscar_equipo
from datetime import datetime

print("=="*30)
print("REGISTRAR SOLICITUD")
print("=="*30)

solicitud_id = input("Por favor, ingresa el id del equipo: ")
solicitud_equipo = buscar_equipo(solicitud_id)
if solicitud_equipo:
    print("Equipo encontrado:")
    
    cedula = input("Por favor, ingresa la cedula del usuario: ")
    cedula = buscar_usuario_cedula(cedula)
    if cedula:
        nombre = input("Por favor, ingresa el nombre del usuario: ")
        tipo_usuario = input("Por favor, ingresa el tipo de usuario: ")
        dias_solicitados = input("Por favor, ingresa los dias solicitados: ")
        fecha_prestamo = input("Por favor, ingresa la fecha de prestamo: %Y-%m-%d ")
    else:
        print("Usuario no encontrado")
    
    if tipo_usuario == "administrativo":
        dias_solicitados = int(dias_solicitados)
        if dias_solicitados > 10:
            print("No puedes solicitar mas de 10 dias")
        elif dias_solicitados < 1:
            print("No puedes solicitar menos de 1 dia")
        
    elif tipo_usuario == "instructor":
        dias_solicitados = int(dias_solicitados)
        if dias_solicitados > 7:
            print("No puedes solicitar mas de 7 dias")
        elif dias_solicitados < 1:
            print("No puedes solicitar menos de 1 dia")
            
    elif tipo_usuario == "estudiante":
        dias_solicitados = int(dias_solicitados)
        if dias_solicitados > 3:
            print("No puedes solicitar mas de 3 dias")
        elif dias_solicitados < 1:
            print("No puedes solicitar menos de 1 dia")
    else:
        print("Tipo de usuario no valido")
            
    
else:
    print("Equipo no encontrado")

print(solicitud)