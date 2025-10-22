import random
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class PinoService(ArbolService):
    """Servicio para operaciones sobre el cultivo Pino."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, pino: Pino) -> int:
        """Aplica la estrategia de absorción de agua con condiciones simuladas."""
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[PinoService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(pino, temperatura, humedad)

    def crecer(self, arbol: Pino, incremento: float) -> None:
        arbol.altura += incremento

    def mostrar_datos(self, pino: Pino):
        print(f"[PINO] Variedad: {pino.variedad} | Altura: {pino.altura}m | "
                f"Agua: {pino.agua}L | Edad: {pino.edad}/{pino.ciclo_de_vida} días")
    
