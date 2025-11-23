"""
Sistema de gestión de inventario
Punto de entrada principal de la aplicación
"""
import sys
from menu_admin import mostrar_menu_principal


def main():
    """Función principal de la aplicación"""
    # Limpiar pantalla al iniciar
    limpiar_pantalla()
    
    print("=" * 40)
    print(" " * 5 + "SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=" * 40)
    
    # Intentar login (máximo 3 intentos)
    intentos = 3
    usuario_autenticado = None
    
    for intento in range(intentos):
        usuario_autenticado = login_admin()
        
        if usuario_autenticado:
            # Login exitoso, mostrar menú principal
            mostrar_menu_principal(usuario_autenticado)
            break
        else:
            # Login fallido
            intentos_restantes = intentos - intento - 1
            if intentos_restantes > 0:
                print(f"\n⚠️  Intentos restantes: {intentos_restantes}")
                input("\nPresione ENTER para intentar nuevamente...")
            else:
                print("\n🚫 Número máximo de intentos alcanzado.")
                print("   Acceso denegado.\n")
                sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        print("¡Hasta pronto!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
