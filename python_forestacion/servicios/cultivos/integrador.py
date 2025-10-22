"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class ArbolService(CultivoService, ABC):
    """Servicio base para árboles."""

    @abstractmethod
    def crecer(self, arbol: Arbol, incremento: float) -> None:
        """Simula el crecimiento de un árbol."""
        pass


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """Servicio base para cualquier tipo de cultivo."""

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra información general del cultivo."""
        pass


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

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
    


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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


