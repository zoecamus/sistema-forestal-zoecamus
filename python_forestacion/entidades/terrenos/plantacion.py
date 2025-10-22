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
