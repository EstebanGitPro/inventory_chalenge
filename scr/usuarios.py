from data.readers import login_usuario_admin, cargar_csv_completo
from data.writers import registro_usuario_admin 


def login():
    
    contador_intentos = 0
    for i in range(3):
        print("=="*30)
        print("INICIAR SESION")
        print("=="*30)
        nombre = input("Por favor, ingresa tu nombre: ")
        contrasena = input("Por favor, ingresa tu contrasena: ")
        usuario = login_usuario_admin(nombre, contrasena)
        if usuario:
            print("Login exitoso")
            break
        else:
            print("Login fallido")
            contador_intentos += 1
        if contador_intentos == 3:
            print("Has excedido el numero maximo de intentos")
            return
    
    
    
def registrar_admin():
    
    print  ("=="*30)
    print("REGISTRAR ADMINISTRADOR")
    print("=="*30)
    if cargar_csv_completo('data/usuario_admin.csv') == []:
        nombre = input("Por favor, ingresa tu nombre: ")
        contrasena = input("Por favor, ingresa tu contrasena: ")
        rol = input("Por favor, ingresa tu rol: ")
        if rol != "admin":
            print("Error: El rol debe ser admin")
        
        else:
            registrar_admin = registro_usuario_admin(nombre, contrasena, rol)
            if registrar_admin:
                print("Registro exitoso")
                
                
            else: 
                print("Registro fallido")
                

    else:
        print("Solo puede estra registrado un solo admin")
        
        
registrar_admin() 
  
login()
    
