from data.readers import buscar_equipo, buscar_usuario_cedula
from datetime import datetime
from data.utils import iguala_formato
from data.writers.solicitudes_writer import registro_solicitud
from equipos import actualizar_estado_equipo


def registrar_solicitud_prestamo(equipo_id, nombre, tipo_usuario, fecha_prestamo, dias_prestamo):
    
    # Registrar la solicitud como pendiente
    if registro_solicitud(equipo_id, nombre, tipo_usuario, fecha_prestamo, dias_prestamo, "pendiente"):
        return True
    else:
        # Revertir el estado del equipo si falla el registro
        registro_solicitud(equipo_id, nombre, tipo_usuario, fecha_prestamo, dias_prestamo, "rechazado")
        return False
    
    
    
    
    
#solicitar_prestamo = registrar_solicitud_prestamo('3152b1be-20a1-414c-b6cd-fd09851d3395', 'Nicolás Martínez', 'administrativo', '2023-01-01', 3)
#print(solicitar_prestamo)






def solicitud_equipo():
    print("=="*30)
    print("REGISTRAR SOLICITUD")
    print("=="*30)
    
    
    hoy = datetime.now().strftime("%Y-%m-%d")
    hoy_str = iguala_formato(hoy)
                                      
                                      
    solicitud_id = input("Por favor, ingresa el id del equipo: ").strip()
    equipo_encontrado = buscar_equipo(solicitud_id)
    
    if not equipo_encontrado:
        print("Equipo no encontrado")
        return
    
    print("Equipo encontrado:")
    estado = equipo_encontrado['estado_actual'].lower()
    
    if estado == "disponible":
        print(f"Equipo {estado}")
        cedula = input("Por favor, ingresa la cedula del usuario: ").strip()
        usuario_encontrado = buscar_usuario_cedula(cedula)
        
        if not usuario_encontrado:
            print("Usuario no encontrado")
            return
        
        nombre = input("Por favor, ingresa el nombre del usuario: ").strip()
        tipo_usuario = input("Por favor, ingresa el tipo de usuario: ").strip().lower()
        dias_solicitados_input = input("Por favor, ingresa los dias solicitados: ").strip()
        fecha_prestamo_input = input(f"Por favor, ingresa la fecha de prestamo yyyy-mm-dd: ").strip()
        fecha_prestamo = iguala_formato(fecha_prestamo_input)
        
        if fecha_prestamo < hoy_str:
            print("La fecha ingresada no puede ser menor a la de hoy")
            return
        
        try:
            dias_solicitados = int(dias_solicitados_input)
        except ValueError:
            print("Los dias solicitados deben ser un numero")
            return
        
        if dias_solicitados < 1:
            print("No puedes solicitar menos de 1 dia")
            return
        
        max_dias = {"estudiante": 3, "instructor": 7, "administrativo": 10}
        
        if tipo_usuario not in max_dias:
            print("Tipo de usuario no valido")
            return
        
        if dias_solicitados > max_dias[tipo_usuario]:
            print(f"No puedes solicitar mas de {max_dias[tipo_usuario]} dias como {tipo_usuario}")
            return
        
        resultado = registrar_solicitud_prestamo(solicitud_id, nombre, tipo_usuario, fecha_prestamo, dias_solicitados)
        
        if resultado:
            print("Solicitud registrada exitosamente")
        else:
            print("Hubo un error al registrar la solicitud")
    else:
        print(f"Equipo no disponible - Estado: {estado}")



solicitud_equipo()
