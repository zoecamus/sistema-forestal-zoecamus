import random
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class OlivoService(ArbolService):
    """Servicio para operaciones sobre el cultivo Olivo."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, olivo: Olivo) -> int:
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[OlivoService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(olivo, temperatura, humedad)

    def crecer(self, arbol: Olivo, incremento: float) -> None:
        arbol.altura += incremento


    def mostrar_datos(self, olivo: Olivo):
        print(f"[OLIVO] Tipo de aceituna: {olivo.fruto.name} | Altura: {olivo.altura}m | "
                f"Agua: {olivo.agua}L | Edad: {olivo.edad}/{olivo.ciclo_de_vida} días")

