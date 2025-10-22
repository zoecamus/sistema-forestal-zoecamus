from abc import ABC, abstractmethod
from typing import Protocol

class AbsorcionAguaStrategy(ABC):
    """Interfaz base del patrón Strategy para definir cómo los cultivos absorben agua."""

    @abstractmethod
    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        #Calcula la cantidad de agua a absorber según condiciones ambientales
        pass
