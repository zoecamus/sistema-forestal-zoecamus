from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """Servicio base para cualquier tipo de cultivo."""

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra información general del cultivo."""
        pass
