import sys
import os

# Add scr to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scr_path = os.path.join(current_dir, 'scr')
sys.path.append(scr_path)

from reportes import generar_reporte_mensual

# Test for December 2025 (where we have a returned loan from previous test)
mes = 12
anio = 2025

print(f"Testing generar_reporte_mensual for {mes}/{anio}...")

exito, mensaje = generar_reporte_mensual(mes, anio)

print(f"Success: {exito}")
print(f"Message: {mensaje}")

if exito:
    # Verify file existence and content
    reporte_filename = f"reporte_prestamos_{anio}_{mes:02d}.csv"
    reporte_path = os.path.join(scr_path, 'data', reporte_filename)
    
    if os.path.exists(reporte_path):
        print(f"\nReport file found: {reporte_path}")
        with open(reporte_path, 'r') as f:
            print("\n--- Report Content ---")
            print(f.read())
    else:
        print(f"\nError: Report file not found at {reporte_path}")
