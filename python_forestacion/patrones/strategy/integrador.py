"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import Protocol

class AbsorcionAguaStrategy(ABC):
    """Interfaz base del patrón Strategy para definir cómo los cultivos absorben agua."""

    @abstractmethod
    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        #Calcula la cantidad de agua a absorber según condiciones ambientales
        pass


