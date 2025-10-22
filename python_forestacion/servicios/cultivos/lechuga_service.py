import random
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class LechugaService(CultivoService):
    """Servicio para operaciones sobre el cultivo Lechuga."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, lechuga: Lechuga) -> int:
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[LechugaService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(lechuga, temperatura, humedad)

    def mostrar_datos(self, lechuga: Lechuga):
        print(f"[LECHUGA] Variedad: {lechuga.variedad} | Agua: {lechuga.agua}L | "
                f"Invernadero: {lechuga.invernadero} | Edad: {lechuga.edad}/{lechuga.ciclo_de_vida} días")
