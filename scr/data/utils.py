import os
import uuid
from datetime import datetime
def obtener_ruta_absoluta(ruta_relativa):
    """
    Convierte una ruta relativa al directorio scr/ en una ruta absoluta.
    
    Args:
        ruta_relativa (str): Ruta relativa desde el directorio scr/
        
    Returns:
        str: Ruta absoluta al archivo
        
    Ejemplo:
        obtener_ruta_absoluta('data/usuario_admin.csv')
        -> '/Users/estebandev/Documents/python/inventory_chalenge/scr/data/usuario_admin.csv'
    """
    if os.path.isabs(ruta_relativa):
        return ruta_relativa
    
    # Obtener el directorio del script actual
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    # Subir un nivel hasta scr/
    dir_scr = os.path.dirname(dir_actual)
    # Construir la ruta completa
    return os.path.join(dir_scr, ruta_relativa)


def id():
    uuid_unico = str(uuid.uuid4())
    return uuid_unico


def iguala_formato(string):
    formatos_soportados = [
        {
            "formato": "%d/%m/%Y",
            "ejemplo": "11/05/2022"},
        {
            "formato": "%Y-%m-%d", 
            "ejemplo": "2022-05-11"}
    ]
    
    mi_formato = "%d/%m/%Y"
    for formato in formatos_soportados:
        try:
            dt = datetime.strptime(string, formato["formato"])
            return dt.strftime(mi_formato)
        except ValueError:
            continue
    return None


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo"""
    os.system('clear' if os.name == 'posix' else 'cls')


import json
import math

def crear_json(ruta_archivo, datos):
    """
    Crea un archivo JSON con los datos proporcionados.
    Si el archivo ya existe, sera sobrescrito.
    
    Args:
        ruta_archivo (str): Ruta completa del archivo JSON a crear.
        datos (dict | list): Datos a escribir en el archivo.
        
    Returns:
        bool: True si la operacion fue exitosa, False en caso contrario.
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)
        return True
    except Exception as e:
        print(f"Error al crear JSON: {e}")
        return False


def leer_json(ruta_archivo):
    """
    Lee el contenido de un archivo JSON.
    
    Args:
        ruta_archivo (str): Ruta completa del archivo JSON a leer.
        
    Returns:
        dict | list | None: Contenido del archivo o None si hay error o no existe.
    """
    if not os.path.exists(ruta_archivo):
        return None
        
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"Error al leer JSON: {e}")
        return None


def actualizar_json(ruta_archivo, nuevos_datos):
    """
    Actualiza un archivo JSON existente.
    Si es una lista, agrega los nuevos datos.
    Si es un diccionario, actualiza las claves.
    
    Args:
        ruta_archivo (str): Ruta completa del archivo JSON.
        nuevos_datos (dict | list): Datos para actualizar.
        
    Returns:
        bool: True si la operacion fue exitosa, False en caso contrario.
    """
    datos_existentes = leer_json(ruta_archivo)
    
    if datos_existentes is None:
        return False
        
    try:
        if isinstance(datos_existentes, list) and isinstance(nuevos_datos, list):
            datos_existentes.extend(nuevos_datos)
        elif isinstance(datos_existentes, dict) and isinstance(nuevos_datos, dict):
            datos_existentes.update(nuevos_datos)
        else:
            # Si los tipos no coinciden o no son soportados para merge simple, sobrescribir
            datos_existentes = nuevos_datos
            
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos_existentes, archivo, indent=4)
        return True
    except Exception as e:
        print(f"Error al actualizar JSON: {e}")
        return False


def eliminar_json(ruta_archivo):
    """
    Elimina un archivo JSON del sistema de archivos.
    
    Args:
        ruta_archivo (str): Ruta completa del archivo a eliminar.
        
    Returns:
        bool: True si fue eliminado, False si no existia o hubo error.
    """
    if not os.path.exists(ruta_archivo):
        return False
        
    try:
        os.remove(ruta_archivo)
        return True
    except Exception as e:
        print(f"Error al eliminar JSON: {e}")
        return False


def calcular_estadisticas(productos):
    """
    Calcula estadisticas de ventas y precios de una lista de productos.
    
    Args:
        productos (list): Lista de diccionarios, donde cada diccionario representa un producto.
                          Se espera que tengan claves como 'nombre', 'precio', 'cantidad_vendida'.
        
    Returns:
        dict: Diccionario con:
              - total_productos: Cantidad total de items unicos.
              - producto_mas_vendido: Nombre del producto con mayor cantidad_vendida.
              - producto_menos_vendido: Nombre del producto con menor cantidad_vendida.
              - precio_mas_alto: El precio mas alto encontrado.
              - precio_mas_bajo: El precio mas bajo encontrado.
              - promedio_precio: Precio promedio de los productos.
              - valor_total_inventario: Suma de (precio * cantidad_vendida) (o stock si fuera el caso).
              Retorna None si la lista esta vacia o los datos no son validos.
    """
    if not productos or not isinstance(productos, list):
        return None
        
    try:
        # Validar que sean diccionarios y tengan las claves necesarias
        # Asumiremos que si falta alguna clave, lo ignoramos o usamos 0
        
        if not all(isinstance(p, dict) for p in productos):
            return None
            
        total_productos = len(productos)
        
        # Filtrar productos validos con precio y cantidad
        prods_validos = [p for p in productos if isinstance(p.get('precio'), (int, float)) and isinstance(p.get('cantidad_vendida'), (int, float))]
        
        if not prods_validos:
            return None
            
        # Producto mas vendido
        mas_vendido = max(prods_validos, key=lambda x: x['cantidad_vendida'])
        menos_vendido = min(prods_validos, key=lambda x: x['cantidad_vendida'])
        
        # Precios
        precios = [p['precio'] for p in prods_validos]
        precio_max = max(precios)
        precio_min = min(precios)
        promedio_precio = sum(precios) / len(precios)
        
        # Valor total (asumiendo que cantidad_vendida es lo que queremos sumarizar como valor de ventas)
        valor_total_ventas = sum(p['precio'] * p['cantidad_vendida'] for p in prods_validos)
        
        return {
            "total_productos_analizados": total_productos,
            "producto_mas_vendido": mas_vendido.get('nombre', 'Desconocido'),
            "cantidad_mas_vendida": mas_vendido['cantidad_vendida'],
            "producto_menos_vendido": menos_vendido.get('nombre', 'Desconocido'),
            "cantidad_menos_vendida": menos_vendido['cantidad_vendida'],
            "precio_mas_alto": precio_max,
            "precio_mas_bajo": precio_min,
            "promedio_precio": round(promedio_precio, 2),
            "valor_total_ventas": round(valor_total_ventas, 2)
        }
    except Exception as e:
        print(f"Error al calcular estadisticas: {e}")
        return None






    
 




