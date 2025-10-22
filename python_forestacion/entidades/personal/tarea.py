from datetime import date

class Tarea:
    """Representa una tarea asignada a un trabajador."""

    def __init__(self, id: int, descripcion: str, fecha_programada: date):
        self.id = id
        self.descripcion = descripcion
        self.fecha_programada = fecha_programada
        self.completada = False  # estado inicial

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __repr__(self):
        estado = "COMPLETADA" if self.completada else "PENDIENTE"
        return f"Tarea(id={self.id}, desc='{self.descripcion}', fecha={self.fecha_programada}, estado={estado})"
    
    @property
    def estado(self):
        return self.completada