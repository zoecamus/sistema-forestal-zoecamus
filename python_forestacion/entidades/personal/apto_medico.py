from dataclasses import dataclass
from datetime import date

@dataclass
class AptoMedico:
    """Certifica si un trabajador está apto para trabajar."""
    apto: bool
    fecha_emision: date
    observaciones: str

    def esta_apto(self) -> bool:
        return self.apto

    def get_resumen(self) -> str:
        estado = "APTO" if self.apto else "NO APTO"
        return f"AptoMedico({estado}, emitido={self.fecha_emision}, obs='{self.observaciones}')"

    def __str__(self):
        return self.get_resumen()
