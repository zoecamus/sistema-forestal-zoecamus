"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.cultivos.cultivo import Cultivo



class Plantacion:
    """
    Representa una plantación agrícola con cultivos y trabajadores.
    """
    def __init__(self, id: int, nombre: str, agua: int, tierra: Tierra, superficie_total: float = None):
        self.id = id
        self.nombre = nombre
        self.agua_disponible = agua
        self.tierra = tierra                  
        self.situada_en = tierra             
        self.cultivos = []
        self.trabajadores = []
        self.superficie_total = superficie_total if superficie_total is not None else getattr(tierra, "superficie", 0.0)


    @property
    def superficie_ocupada(self) -> float:
        return sum(getattr(c, "superficie", 0.0) for c in self.cultivos)

    @property
    def superficie_disponible(self) -> float:
        return self.superficie_total - self.superficie_ocupada

    def __str__(self):
        return (f"Plantacion(id={self.id}, nombre='{self.nombre}', "
                f"superficie_total={self.superficie_total}, "
                f"ocupada={self.superficie_ocupada:.2f}, "
                f"agua={self.agua_disponible})")

    def get_cultivos(self):
        return list(self.cultivos)

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def get_cultivos_interno(self):
        return self.cultivos

    def get_trabajadores(self):
        return list(self.trabajadores)

    def get_trabajadores_interno(self):
        return self.trabajadores

    def set_trabajadores(self, trabajadores):
        self.trabajadores = trabajadores

    def get_tierra(self):
        return self.situada_en

    def get_agua_disponible(self):
        return self.agua_disponible

    def set_agua_disponible(self, cantidad):
        self.agua_disponible = cantidad

    def __repr__(self):
        return f"Plantacion(id={self.id}, nombre='{self.nombre}', agua={self.agua_disponible})"


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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



