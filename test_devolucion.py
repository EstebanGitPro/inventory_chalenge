import sys
import os

# Add scr to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scr_path = os.path.join(current_dir, 'scr')
sys.path.append(scr_path)

from prestamos import registrar_devolucion

# ID from previous context
equipo_id = "k7l3m8n1-5l2o-4j9k-l8m4-n3o2k1l0j9i9"
fecha_devolucion_real = "03/12/2025" # 1 day late (pactada was 02/12/2025)

print(f"Testing registrar_devolucion for {equipo_id} on {fecha_devolucion_real}...")

exito, mensaje = registrar_devolucion(equipo_id, fecha_devolucion_real)

print(f"Success: {exito}")
print(f"Message: {mensaje}")

if exito:
    print("\nVerifying files content (preview):")
    # Check prestamos.csv
    with open(os.path.join(scr_path, 'data/prestamos.csv'), 'r') as f:
        print("\n--- prestamos.csv (last 2 lines) ---")
        lines = f.readlines()
        for line in lines[-2:]:
            print(line.strip())
            
    # Check historial_equpos.csv
    with open(os.path.join(scr_path, 'data/historial_equpos.csv'), 'r') as f:
        print("\n--- historial_equpos.csv (last 2 lines) ---")
        lines = f.readlines()
        for line in lines[-2:]:
            print(line.strip())

    # Check historial_usuarios.csv
    with open(os.path.join(scr_path, 'data/historial_usuarios.csv'), 'r') as f:
        print("\n--- historial_usuarios.csv (last 2 lines) ---")
        lines = f.readlines()
        for line in lines[-2:]:
            print(line.strip())
