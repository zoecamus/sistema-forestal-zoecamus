from python_forestacion.patrones.singleton.singleton import SingletonMeta
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy



class CultivoServiceRegistry(metaclass=SingletonMeta):
    """Centraliza los servicios de cultivos (patrón Registry + Singleton)."""

    def __init__(self):
        """Inicializa los servicios solo una vez (gracias al Singleton)."""
        # Verifica si ya fueron cargados
        if not hasattr(self, "_handlers"):
            self._handlers = {
                "Pino": PinoService(AbsorcionConstanteStrategy()),
                "Olivo": OlivoService(AbsorcionSeasonalStrategy()),
                "Lechuga": LechugaService(AbsorcionConstanteStrategy()),
                "Zanahoria": ZanahoriaService(AbsorcionConstanteStrategy()),
            }

    def obtener_servicio(self, nombre: str):
        """Devuelve el servicio correspondiente a un cultivo."""
        return self._handlers.get(nombre)

    def mostrar_servicios(self):
        print("\n=== Servicios registrados ===")
        for nombre, servicio in self._handlers.items():
            print(f"- {nombre}: {servicio.__class__.__name__}")
