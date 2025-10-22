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
