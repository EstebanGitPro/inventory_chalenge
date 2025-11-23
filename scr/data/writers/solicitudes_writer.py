


def registro_solicitud(solicitud_id, nombre, tipo_usuario, dias_prestamo):
        ruta_csv = obtener_ruta_absoluta('data/solicitudes.csv')    
    if ruta_csv:
        
            with open(ruta_csv, 'a', newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=['solicitud_id', 'nombre', 'tipo_usuario', 'dias_prestamo'])
                if  cargar_csv_completo('data/solicitudes.csv') == []:
                    escritor.writeheader()
                    escritor.writerow({'equipo_id': equipo_id, 'nombre_equipo': nombre_equipo, 'categoria': categoria, 'estado_actual': estado_actual, 'fecha_registro': fecha_registro, 'descripcion': descripcion})
                else:
                    escritor.writerow({'equipo_id': equipo_id, 'nombre_equipo': nombre_equipo, 'categoria': categoria, 'estado_actual': estado_actual, 'fecha_registro': fecha_registro, 'descripcion': descripcion})
                return True