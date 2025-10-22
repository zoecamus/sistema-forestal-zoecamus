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
