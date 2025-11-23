"""
Módulo de autenticación para administradores
"""
import os
from data.readers import buscar_usuario_admin


def login_admin():
    """
    Autentica a un usuario administrador.
    
    Returns:
        dict | None: Datos del usuario si la autenticación es exitosa, None en caso contrario
    """
    print("\n" + "=" * 40)
    print(" " * 10 + "LOGIN ADMINISTRADOR")
    print("=" * 40)
    
    # Obtener credenciales
    usuario = input("\n👤 Usuario: ").strip()
    contrasena = input("🔑 Contraseña: ").strip()
    
    # Validar campos vacíos
    if not usuario or not contrasena:
        print("\n❌ Error: Usuario y contraseña son requeridos")
        return None
    
    # Buscar usuario en el CSV
    datos_usuario = buscar_usuario_admin(usuario)
    
    if datos_usuario is None:
        print(f"\n❌ Error: Usuario '{usuario}' no encontrado")
        return None
    
    # Verificar contraseña
    if datos_usuario['contrasena'] == contrasena:
        print(f"\n✅ Bienvenido {datos_usuario['usuario']}")
        print(f"   Rol: {datos_usuario['rol']}")
        return datos_usuario
    else:
        print("\n❌ Error: Contraseña incorrecta")
        return None


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo"""
    os.system('clear' if os.name == 'posix' else 'cls')
