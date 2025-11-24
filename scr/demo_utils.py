import os
import sys

# Agregar el directorio actual al path para importar modulos hermanos
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from data.utils import crear_json, leer_json, actualizar_json, eliminar_json, calcular_estadisticas, obtener_ruta_absoluta

def demostrar_uso_utils():
    print("=== DEMOSTRACION DE UTILIDADES GENERICAS ===")
    
    # 1. Definir datos de prueba
    archivo_demo = "datos_demo.json"
    ruta_completa = obtener_ruta_absoluta(f"data/{archivo_demo}")
    
    datos_iniciales = {
        "curso": "Python Avanzado",
        "estudiantes": [
            {"nombre": "Ana", "nota": 85},
            {"nombre": "Beto", "nota": 92},
            {"nombre": "Carla", "nota": 78}
        ],
        "activo": True
    }
    
    print(f"\n1. Creando archivo JSON en: {ruta_completa}")
    if crear_json(ruta_completa, datos_iniciales):
        print("   -> Archivo creado exitosamente.")
    else:
        print("   -> Error al crear archivo.")
        return

    # 2. Leer datos
    print("\n2. Leyendo archivo JSON...")
    datos_leidos = leer_json(ruta_completa)
    if datos_leidos:
        print("   -> Datos leidos correctamente:")
        print(f"      Curso: {datos_leidos.get('curso')}")
        print(f"      Estudiantes: {len(datos_leidos.get('estudiantes', []))}")
    
    # 3. Actualizar datos
    print("\n3. Actualizando archivo JSON...")
    nuevos_datos = {
        "semestre": "2025-1",
        "estudiantes": [ # Esto sobrescribira la lista si es un dict update simple, 
                         # pero nuestra funcion actualizar_json hace update de dicts.
                         # Si la clave ya existe, la reemplaza.
                         # Vamos a agregar un estudiante nuevo a la lista y actualizar todo el dict.
        ]
    }
    
    # Modifiquemos la lista en memoria y luego actualicemos todo el objeto
    datos_leidos['estudiantes'].append({"nombre": "Daniel", "nota": 95})
    datos_leidos['semestre'] = "2025-1"
    
    # Usamos actualizar_json pasando el dict completo modificado 
    # (o podriamos pasar solo campos nuevos si quisieramos merge, 
    # pero para listas anidadas es mejor manejarlo asi)
    if actualizar_json(ruta_completa, datos_leidos):
        print("   -> Archivo actualizado exitosamente.")
        
    # 4. Calcular estadisticas de productos
    print("\n4. Calculando estadisticas de productos...")
    
    # Definir una lista de productos para la demo
    productos_demo = [
        {"nombre": "Laptop Gamer", "precio": 1500.00, "cantidad_vendida": 10},
        {"nombre": "Mouse Inalambrico", "precio": 25.50, "cantidad_vendida": 50},
        {"nombre": "Teclado Mecanico", "precio": 80.00, "cantidad_vendida": 30},
        {"nombre": "Monitor 24p", "precio": 200.00, "cantidad_vendida": 15},
        {"nombre": "Cable HDMI", "precio": 10.00, "cantidad_vendida": 5} # Menos vendido
    ]
    
    print(f"   -> Analizando {len(productos_demo)} productos de prueba...")
    
    stats = calcular_estadisticas(productos_demo)
    if stats:
        print("   -> Estadisticas calculadas:")
        for k, v in stats.items():
            # Formatear nombre de clave para que se vea mejor
            clave_fmt = k.replace('_', ' ').capitalize()
            print(f"      {clave_fmt}: {v}")
            
    # 5. Eliminar archivo (opcional, lo dejaremos para verificar)
    # print("\n5. Eliminando archivo de prueba...")
    # if eliminar_json(ruta_completa):
    #     print("   -> Archivo eliminado.")
    
    print("\n=== FIN DE DEMOSTRACION ===")

if __name__ == "__main__":
    demostrar_uso_utils()
