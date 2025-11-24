"""
Módulo de menú principal para administradores
"""
from auth import limpiar_pantalla
from equipos import agregar_equipo, actualizar_estado_equipo
from data.readers import leer_todos_equipos, buscar_equipo, leer_todos_usuarios, buscar_usuario_cedula
from solicitudes import solicitud_equipo
from prestamos import gestionar_solicitudes_pendientes, registrar_devolucion, listar_prestamos_activos
from reportes import generar_reporte_mensual
from usuarios import registrar_admin
from datetime import datetime

def mostrar_menu_principal(usuario_datos):
    """
    Muestra el menú principal del administrador
    
    Args:
        usuario_datos (dict): Diccionario con información del usuario logueado
    """
    while True:
        print("\n" + "=" * 40)
        print(f" MENU PRINCIPAL - {usuario_datos['usuario']}")
        print("=" * 40)
        print("\n1. Gestionar Equipos")
        print("2. Gestionar Prestamos")
        print("3. Ver Reportes")
        print("4. Gestionar Usuarios")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            menu_equipos()
        elif opcion == "2":
            menu_prestamos()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "4":
            menu_usuarios()
        elif opcion == "5":
            print("\nCerrando sesion...")
            print("Hasta pronto!\n")
            break
        else:
            print("\nOpcion invalida. Por favor, seleccione un numero del 1 al 5.")
            input("\nPresione ENTER para continuar...")


def menu_equipos():
    """Menú para gestionar equipos"""
    while True:
        print("\n" + "=" * 40)
        print(" GESTION DE EQUIPOS")
        print("=" * 40)
        print("\n1. Agregar equipo")
        print("2. Modificar estado equipo")
        print("3. Listar equipos")
        print("4. Buscar equipo")
        print("5. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            # Agregar equipo
            print("\n--- Agregar Equipo ---")
            equipo_id = input("ID del equipo: ").strip()
            if buscar_equipo(equipo_id):
                print("Error: Ya existe un equipo con ese ID.")
            else:
                nombre = input("Nombre del equipo: ").strip()
                categoria = input("Categoria: ").strip()
                descripcion = input("Descripcion (opcional): ").strip()
                fecha = datetime.now().strftime("%d/%m/%Y")
                # Llamar a funcion de equipos.py (necesita ser importada o creada si no existe wrapper)
                # equipos.py tiene agregar_equipo
                agregar_equipo(equipo_id, nombre, categoria, "disponible", fecha, descripcion)
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "2":
            # Modificar estado
            print("\n--- Modificar Estado Equipo ---")
            equipo_id = input("ID del equipo: ").strip()
            equipo = buscar_equipo(equipo_id)
            if equipo:
                print(f"Estado actual: {equipo['estado_actual']}")
                nuevo_estado = input("Nuevo estado (disponible/mantenimiento): ").strip().lower()
                if nuevo_estado in ['disponible', 'mantenimiento']:
                    if actualizar_estado_equipo(equipo_id, nuevo_estado):
                        print("Estado actualizado exitosamente.")
                    else:
                        print("Error al actualizar estado.")
                else:
                    print("Estado invalido. Solo se permite 'disponible' o 'mantenimiento'.")
            else:
                print("Equipo no encontrado.")
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "3":
            # Listar equipos
            print("\n--- Listado de Equipos ---")
            equipos, _ = leer_todos_equipos()
            if equipos:
                print(f"{'ID':<40} {'Nombre':<30} {'Categoria':<20} {'Estado':<15}")
                print("-" * 105)
                for e in equipos:
                    print(f"{e['equipo_id']:<40} {e['nombre_equipo']:<30} {e['categoria']:<20} {e['estado_actual']:<15}")
            else:
                print("No hay equipos registrados.")
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "4":
            # Buscar equipo
            print("\n--- Buscar Equipo ---")
            equipo_id = input("ID del equipo: ").strip()
            equipo = buscar_equipo(equipo_id)
            if equipo:
                print("\nInformacion del Equipo:")
                for k, v in equipo.items():
                    print(f"{k.capitalize()}: {v}")
            else:
                print("Equipo no encontrado.")
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "5":
            break
        else:
            print("\nOpcion invalida.")
            input("\nPresione ENTER para continuar...")


def menu_prestamos():
    """Menú para gestionar préstamos"""
    while True:
        print("\n" + "=" * 40)
        print(" GESTION DE PRESTAMOS")
        print("=" * 40)
        print("\n1. Registrar solicitud de prestamo")
        print("2. Gestionar solicitudes pendientes (Aprobar/Rechazar)")
        print("3. Registrar devolucion")
        print("4. Listar prestamos activos")
        print("5. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            solicitud_equipo()
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "2":
            gestionar_solicitudes_pendientes()
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "3":
            print("\n--- Registrar Devolucion ---")
            equipo_id = input("ID del equipo a devolver: ").strip()
            fecha_dev = input("Fecha de devolucion (dd/mm/yyyy): ").strip()
            exito, msg = registrar_devolucion(equipo_id, fecha_dev)
            print(f"\n{msg}")
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "4":
            listar_prestamos_activos()
            # listar_prestamos_activos ya tiene su propio input() al final, pero por consistencia en menu:
            # Ah, listar_prestamos_activos tiene input() al final.
            pass 
            
        elif opcion == "5":
            break
        else:
            print("\nOpcion invalida.")
            input("\nPresione ENTER para continuar...")


def menu_reportes():
    """Menú para ver reportes"""
    while True:
        print("\n" + "=" * 40)
        print(" REPORTES")
        print("=" * 40)
        print("\n1. Generar reporte mensual de prestamos")
        print("2. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            print("\n--- Generar Reporte Mensual ---")
            mes = input("Mes (1-12): ").strip()
            anio = input("Año (yyyy): ").strip()
            exito, msg = generar_reporte_mensual(mes, anio)
            print(f"\n{msg}")
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "2":
            break
        else:
            print("\nOpcion invalida.")
            input("\nPresione ENTER para continuar...")


def menu_usuarios():
    """Menú para gestionar usuarios"""
    while True:
        print("\n" + "=" * 40)
        print(" GESTION DE USUARIOS")
        print("=" * 40)
        print("\n1. Registrar nuevo administrador")
        print("2. Listar usuarios (admins)")
        print("3. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            registrar_admin()
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "2":
            print("\n--- Listado de Usuarios ---")
            # No hay funcion publica para listar usuarios en usuarios.py, usamos reader directo
            usuarios, _ = leer_todos_usuarios() # Necesitamos importar esto o crearlo
            # data/readers/usuarios_reader.py tiene leer_todos_usuarios?
            # Revisando imports... agregare leer_todos_usuarios a imports arriba
            if usuarios:
                for u in usuarios:
                    print(f"Usuario: {u['usuario']} - Rol: {u['rol']}")
            else:
                print("No hay usuarios registrados.")
            input("\nPresione ENTER para continuar...")
            
        elif opcion == "3":
            break
        else:
            print("\nOpcion invalida.")
            input("\nPresione ENTER para continuar...")
