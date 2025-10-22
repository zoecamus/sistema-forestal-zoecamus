from dataclasses import dataclass

@dataclass
class Herramienta:
    """Representa una herramienta utilizada por los trabajadores."""

    id: int
    nombre: str
    estado: str = "Operativa" 
    certificacion_seguridad: str = "IRAM-ISO 45001" #norma argentina e internacional sobre seguridad laboral

    def get_nombre(self):
        return self.nombre
    
    def __str__(self):
        return (f"Herramienta(id={self.id}, nombre='{self.nombre}', estado={self.estado}, "
                f"certificación={self.certificacion_seguridad})")



