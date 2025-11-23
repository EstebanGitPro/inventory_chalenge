"""
Módulo de menú principal para administradores
"""
from auth import limpiar_pantalla


def mostrar_menu_principal(usuario_datos):
    """
    Muestra el menú principal del administrador
    
    Args:
        usuario_datos (dict): Diccionario con información del usuario logueado
    """
    while True:
        print("\n" + "=" * 40)
        print(f" MENÚ PRINCIPAL - {usuario_datos['usuario']}")
        print("=" * 40)
        print("\n1. 📦 Gestionar Equipos")
        print("2. 🔄 Gestionar Préstamos")
        print("3. 📊 Ver Reportes")
        print("4. 👥 Gestionar Usuarios")
        print("5. 🚪 Salir")
        
        opcion = input("\n➜ Seleccione una opción: ").strip()
        
        if opcion == "1":
            menu_equipos()
        elif opcion == "2":
            menu_prestamos()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "4":
            menu_usuarios()
        elif opcion == "5":
            print("\n👋 Cerrando sesión...")
            print("¡Hasta pronto!\n")
            break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione un número del 1 al 5.")
            input("\nPresione ENTER para continuar...")


def menu_equipos():
    """Menú para gestionar equipos"""
    while True:
        print("\n" + "=" * 40)
        print(" GESTIÓN DE EQUIPOS")
        print("=" * 40)
        print("\n1. ➕ Agregar equipo")
        print("2. 📝 Modificar equipo")
        print("3. 🗑️  Eliminar equipo")
        print("4. 📋 Listar equipos")
        print("5. 🔍 Buscar equipo")
        print("6. ⬅️  Volver al menú principal")
        
        opcion = input("\n➜ Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n[Función: Agregar equipo - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            print("\n[Función: Modificar equipo - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            print("\n[Función: Eliminar equipo - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            print("\n[Función: Listar equipos - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            print("\n[Función: Buscar equipo - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "6":
            break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione un número del 1 al 6.")
            input("\nPresione ENTER para continuar...")


def menu_prestamos():
    """Menú para gestionar préstamos"""
    while True:
        print("\n" + "=" * 40)
        print(" GESTIÓN DE PRÉSTAMOS")
        print("=" * 40)
        print("\n1. 🆕 Registrar préstamo")
        print("2. ✅ Registrar devolución")
        print("3. 📋 Listar préstamos activos")
        print("4. 📜 Historial de préstamos")
        print("5. ⬅️  Volver al menú principal")
        
        opcion = input("\n➜ Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n[Función: Registrar préstamo - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            print("\n[Función: Registrar devolución - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            print("\n[Función: Listar préstamos activos - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            print("\n[Función: Historial de préstamos - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione un número del 1 al 5.")
            input("\nPresione ENTER para continuar...")


def menu_reportes():
    """Menú para ver reportes"""
    while True:
        print("\n" + "=" * 40)
        print(" REPORTES")
        print("=" * 40)
        print("\n1. 📊 Reporte de equipos disponibles")
        print("2. 📊 Reporte de equipos prestados")
        print("3. 📊 Reporte de usuarios con préstamos")
        print("4. 📊 Reporte general")
        print("5. ⬅️  Volver al menú principal")
        
        opcion = input("\n➜ Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n[Función: Reporte equipos disponibles - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            print("\n[Función: Reporte equipos prestados - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            print("\n[Función: Reporte usuarios con préstamos - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            print("\n[Función: Reporte general - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione un número del 1 al 5.")
            input("\nPresione ENTER para continuar...")


def menu_usuarios():
    """Menú para gestionar usuarios"""
    while True:
        print("\n" + "=" * 40)
        print(" GESTIÓN DE USUARIOS")
        print("=" * 40)
        print("\n1. ➕ Agregar usuario")
        print("2. 📝 Modificar usuario")
        print("3. 🗑️  Eliminar usuario")
        print("4. 📋 Listar usuarios")
        print("5. ⬅️  Volver al menú principal")
        
        opcion = input("\n➜ Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n[Función: Agregar usuario - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            print("\n[Función: Modificar usuario - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            print("\n[Función: Eliminar usuario - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            print("\n[Función: Listar usuarios - Por implementar]")
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione un número del 1 al 5.")
            input("\nPresione ENTER para continuar...")
