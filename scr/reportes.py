from data.readers import leer_todos_prestamos, buscar_equipo
from data.utils import obtener_ruta_absoluta
import csv
from datetime import datetime

def generar_reporte_mensual(mes, anio):
    """
    Genera un reporte CSV de prestamos devueltos para el mes y anio especificados.
    """
    prestamos, _ = leer_todos_prestamos()
    
    if not prestamos:
        return False, "No hay prestamos registrados"
    
    reporte_data = []
    
    for idx, p in enumerate(prestamos, 1):
        # Filtrar solo devueltos
        if p['estado'].lower() != 'devuelto':
            continue
            
        # Filtrar por mes y anio de devolucion
        try:
            fecha_dev = datetime.strptime(p['fecha_devolucion'], "%d/%m/%Y")
            if fecha_dev.month != int(mes) or fecha_dev.year != int(anio):
                continue
        except ValueError:
            continue # Saltar fechas invalidas
            
        # Obtener datos adicionales
        equipo = buscar_equipo(p['equipo_id'])
        nombre_equipo = equipo['nombre_equipo'] if equipo else "Desconocido"
        
        # Construir fila del reporte
        fila = {
            "prestamo_id": f"P-{idx:04d}",
            "equipo_id": p['equipo_id'],
            "nombre_equipo": nombre_equipo,
            "usuario_prestatario": p['nombre'],
            "tipo_usuario": p['tipo_usuario'],
            "fecha_solicitud": "N/A", # No disponible en prestamos.csv
            "fecha_prestamo": p['fecha_prestamo'],
            "fecha_devolucion": p['fecha_devolucion'],
            "dias_autorizados": p['dias_prestamo'],
            "dias_reales_usados": p.get('dias_reales_usados', 'N/A'),
            "retraso": p.get('retraso', 'N/A'),
            "estado": p['estado'],
            "mes": mes,
            "anio": anio
        }
        reporte_data.append(fila)
        
    if not reporte_data:
        return False, f"No se encontraron prestamos devueltos para {mes}/{anio}"
        
    # Escribir reporte
    nombre_archivo = f"reporte_prestamos_{anio}_{int(mes):02d}.csv"
    ruta_reporte = obtener_ruta_absoluta(f"data/{nombre_archivo}")
    
    fieldnames = [
        "prestamo_id", "equipo_id", "nombre_equipo", "usuario_prestatario", 
        "tipo_usuario", "fecha_solicitud", "fecha_prestamo", "fecha_devolucion", 
        "dias_autorizados", "dias_reales_usados", "retraso", "estado", "mes", "anio"
    ]
    
    try:
        with open(ruta_reporte, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
            escritor.writeheader()
            escritor.writerows(reporte_data)
        return True, f"Reporte generado exitosamente: {nombre_archivo}"
    except Exception as e:
        return False, f"Error al generar reporte: {e}"
