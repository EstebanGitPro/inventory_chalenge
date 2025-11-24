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
    usuario = input("\nUsuario: ").strip()
    contrasena = input("Contrasena: ").strip()
    
    # Validar campos vacíos
    if not usuario or not contrasena:
        print("\nError: Usuario y contrasena son requeridos")
        return None
    
    # Buscar usuario en el CSV
    datos_usuario = buscar_usuario_admin(usuario)
    
    if datos_usuario is None:
        print(f"\nError: Usuario '{usuario}' no encontrado")
        return None
    
    # Verificar contraseña
    if datos_usuario['contrasena'] == contrasena:
        print(f"\nBienvenido {datos_usuario['usuario']}")
        print(f"   Rol: {datos_usuario['rol']}")
        return datos_usuario
    else:
        print("\nError: Contrasena incorrecta")
        return None


