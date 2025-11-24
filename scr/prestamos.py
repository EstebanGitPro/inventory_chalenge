from data.readers import leer_todas_solicitudes, buscar_equipo
from data.writers import sobrescribir_solicitudes, registrar_prestamo
from equipos import actualizar_estado_equipo
from datetime import datetime, timedelta
from data.utils import iguala_formato


def actualizar_estado_solicitud(equipo_id, nombre, nuevo_estado):
    solicitudes, fieldnames = leer_todas_solicitudes()
    
    if not solicitudes:
        return False
    
    solicitud_actualizada = False
    
    for solicitud in solicitudes:
        if (solicitud['equipo_id'] == equipo_id and 
            solicitud['nombre'] == nombre and 
            solicitud['estado'].lower() == 'pendiente'):
            solicitud['estado'] = nuevo_estado
            solicitud_actualizada = True
            break
    
    if not solicitud_actualizada:
        return False
    
    return sobrescribir_solicitudes(solicitudes, fieldnames)


def aprobar_solicitud(equipo_id, nombre, tipo_usuario, fecha_prestamo, dias_prestamo):
    try:
        fecha_inicio = datetime.strptime(fecha_prestamo, "%d/%m/%Y")
    except ValueError:
        return False, "Formato de fecha invalido"
    
    fecha_devolucion = fecha_inicio + timedelta(days=int(dias_prestamo))
    fecha_devolucion_str = fecha_devolucion.strftime("%d/%m/%Y")
    
    if not actualizar_estado_equipo(equipo_id, "prestado"):
        return False, "Error al actualizar estado del equipo"
    
    if not registrar_prestamo(equipo_id, nombre, tipo_usuario, fecha_prestamo, fecha_devolucion_str, dias_prestamo, "activo"):
        actualizar_estado_equipo(equipo_id, "disponible")
        return False, "Error al registrar prestamo"
    
    if not actualizar_estado_solicitud(equipo_id, nombre, "aprobado"):
        return False, "Error al actualizar solicitud"
    
    return True, "Prestamo aprobado exitosamente"


def rechazar_solicitud(equipo_id, nombre):
    if not actualizar_estado_solicitud(equipo_id, nombre, "rechazado"):
        return False, "Error al actualizar solicitud"
    
    return True, "Solicitud rechazada"


def gestionar_solicitudes_pendientes():
    from data.readers import buscar_solicitudes_pendientes
    
    print("=="*30)
    print("GESTIONAR SOLICITUDES PENDIENTES")
    print("=="*30)
    
    solicitudes_pendientes = buscar_solicitudes_pendientes()
    
    if not solicitudes_pendientes:
        print("\nNo hay solicitudes pendientes")
        return
    
    print(f"\nTotal de solicitudes pendientes: {len(solicitudes_pendientes)}\n")
    
    for idx, solicitud in enumerate(solicitudes_pendientes, 1):
        equipo = buscar_equipo(solicitud['equipo_id'])
        equipo_nombre = equipo['nombre_equipo'] if equipo else "Desconocido"
        
        print(f"\n--- Solicitud {idx} ---")
        print(f"Equipo: {equipo_nombre}")
        print(f"ID Equipo: {solicitud['equipo_id']}")
        print(f"Usuario: {solicitud['nombre']}")
        print(f"Tipo: {solicitud['tipo_usuario']}")
        print(f"Fecha prestamo: {solicitud['fecha_prestamo']}")
        print(f"Dias solicitados: {solicitud['dias_prestamo']}")
        
        opcion = input("\n[A]probar / [R]echazar / [S]altar: ").strip().upper()
        
        if opcion == 'A':
            exito, mensaje = aprobar_solicitud(
                solicitud['equipo_id'],
                solicitud['nombre'],
                solicitud['tipo_usuario'],
                solicitud['fecha_prestamo'],
                solicitud['dias_prestamo']
            )
            print(f"\n{mensaje}")
        elif opcion == 'R':
            exito, mensaje = rechazar_solicitud(
                solicitud['equipo_id'],
                solicitud['nombre']
            )
            print(f"\n{mensaje}")
        elif opcion == 'S':
            print("\nSolicitud omitida")
        else:
            print("\nOpcion invalida, solicitud omitida")
    
    print("\n" + "=="*30)
    print("Gestion de solicitudes completada")
    print("=="*30)


def listar_prestamos_activos():
    from data.readers import buscar_prestamos_activos
    
    print("=="*30)
    print("PRESTAMOS ACTIVOS")
    print("=="*30)
    
    prestamos = buscar_prestamos_activos()
    
    if not prestamos:
        print("\nNo hay prestamos activos")
        return
    
    print(f"\nTotal de prestamos activos: {len(prestamos)}\n")
    
    for idx, prestamo in enumerate(prestamos, 1):
        equipo = buscar_equipo(prestamo['equipo_id'])
        equipo_nombre = equipo['nombre_equipo'] if equipo else "Desconocido"
        
        print(f"\n--- Prestamo {idx} ---")
        print(f"Equipo: {equipo_nombre}")
        print(f"ID Equipo: {prestamo['equipo_id']}")
        print(f"Usuario: {prestamo['nombre']}")
        print(f"Tipo: {prestamo['tipo_usuario']}")
        print(f"Fecha prestamo: {prestamo['fecha_prestamo']}")
        print(f"Fecha devolucion: {prestamo['fecha_devolucion']}")
        print(f"Dias prestamo: {prestamo['dias_prestamo']}")
        print(f"Estado: {prestamo['estado']}")
    
    input("\nPresiona ENTER para continuar")
