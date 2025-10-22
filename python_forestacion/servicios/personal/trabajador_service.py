from datetime import date
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class TrabajadorService:
    """Servicio que maneja operaciones sobre los trabajadores."""

    def asignar_apto_medico(self, trabajador, apto: bool, fecha: date, obs: str):
        """Asigna un nuevo apto médico al trabajador."""
        apto_medico = AptoMedico(apto, fecha, obs)
        trabajador.set_apto_medico(apto_medico)
        print(f"Apto médico asignado a {trabajador.get_nombre()}: {apto_medico.get_resumen()}")

    def trabajar(self, trabajador, fecha: date, herramienta):
        """Ejecuta las tareas del trabajador según su apto médico y fecha programada."""
        apto = trabajador.get_apto_medico()

        # Validar apto médico antes de trabajar
        if not apto or not apto.esta_apto():
            print(f"[ERROR] {trabajador.get_nombre()} no puede trabajar (no apto).")
            return False

        tareas = trabajador.get_tareas()
        if not tareas:
            print(f"[INFO] {trabajador.get_nombre()} no tiene tareas asignadas.")
            return False

        # Ordenar tareas por ID descendente
        tareas_ordenadas = sorted(tareas, key=lambda t: t.id, reverse=True)

        print(f"[TAREAS] Ejecutando tareas de {trabajador.get_nombre()} con {herramienta.nombre} "
              f"(Certificación: {herramienta.certificacion_seguridad})...")

        for tarea in tareas_ordenadas:
            if tarea.fecha_programada == fecha:
                tarea.completada = True
                estado = "COMPLETADA"
            else:
                estado = "PENDIENTE"

            print(f" - Tarea {tarea.id}: '{tarea.descripcion}' → {estado} "
                  f"(programada para {tarea.fecha_programada})")

        print(f"{trabajador.get_nombre()} trabajó el {fecha} con {herramienta.nombre}.\n")
        return True
