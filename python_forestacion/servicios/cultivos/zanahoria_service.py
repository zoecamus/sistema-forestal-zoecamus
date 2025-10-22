import random
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ZanahoriaService(CultivoService):
    """Servicio para operaciones sobre el cultivo Zanahoria."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, zanahoria: Zanahoria) -> int:
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[ZanahoriaService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(zanahoria, temperatura, humedad)


    def mostrar_datos(self, zanahoria: Zanahoria):
        tipo = "Baby Carrot" if zanahoria.baby_carrot else "Común"
        print(f"[ZANAHORIA] Tipo: {tipo} | Agua: {zanahoria.agua}L | "
            f"Superficie: {zanahoria.superficie} | Edad: {zanahoria.edad}/{zanahoria.ciclo_de_vida} días")
