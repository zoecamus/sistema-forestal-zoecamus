from dataclasses import dataclass
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class RegistroForestal:
    """Registro administrativo y económico de una finca."""
    id_padron: int
    tierra: Tierra
    plantacion: Plantacion
    propietario: str
    avaluo: float


    def __post_init__(self):
        """Validación automática tras la creación del dataclass."""
        if self.avaluo <= 0:
            raise ValueError("El avalúo fiscal debe ser mayor a 0.")

    def __str__(self):
        return (
            f"RegistroForestal(id_padron={self.id_padron}, "
            f"propietario='{self.propietario}', "
            f"avaluo=${self.avaluo:,.2f}, "
            f"plantacion='{self.plantacion.nombre}')"
        )
