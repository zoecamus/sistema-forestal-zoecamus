"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_CONST_LECHUGA,
    ABSORCION_CONST_ZANAHORIA,
)

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción constante (para hortalizas)."""

    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        if tipo_cultivo.lower() == "lechuga":
            return ABSORCION_CONST_LECHUGA
        elif tipo_cultivo.lower() == "zanahoria":
            return ABSORCION_CONST_ZANAHORIA
        else:
            return 1.5  


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
)

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción estacional (para árboles)."""

    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        mes = date.today().month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO  # verano
        else:
            return ABSORCION_SEASONAL_INVIERNO  # invierno


