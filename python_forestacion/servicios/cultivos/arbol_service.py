from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class ArbolService(CultivoService, ABC):
    """Servicio base para árboles."""

    @abstractmethod
    def crecer(self, arbol: Arbol, incremento: float) -> None:
        """Simula el crecimiento de un árbol."""
        pass
