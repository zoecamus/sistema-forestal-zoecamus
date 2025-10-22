from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class Tierra:
    """Representa un terreno físico donde se puede ubicar una plantación."""
    id: int
    superficie: float
    domicilio: str
    finca: Optional["Plantacion"] = None  

    # Métodos
    def set_finca(self, finca: "Plantacion"):
        self.finca = finca

    def get_finca(self):
        return self.finca

    def __str__(self):
        return f"Tierra(id={self.id}, superficie={self.superficie}, domicilio='{self.domicilio}')"
   
    def __repr__(self):
        return f"Tierra(Padrón #{self.id}, Superficie={self.superficie} m², Domicilio='{self.domicilio}')"

    def get_id(self):
        return self.id

