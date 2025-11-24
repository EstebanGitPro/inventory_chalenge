from .usuarios_writers import registro_usuario_admin
from .equipo_writer import registrar_equipo, sobrescribir_equipos
from .solicitudes_writer import registro_solicitud, sobrescribir_solicitudes
from .prestamo_writer import registrar_prestamo, sobrescribir_prestamos
from .historial_writer import registrar_historial_equipo, registrar_historial_usuario


__all__ = ['registro_usuario_admin', 'registrar_equipo', 'registro_solicitud', 'sobrescribir_equipos', 'sobrescribir_solicitudes', 'registrar_prestamo', 'sobrescribir_prestamos', 'registrar_historial_equipo', 'registrar_historial_usuario']
