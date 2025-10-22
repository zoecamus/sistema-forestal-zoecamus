"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

from typing import List, Type
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.negocio.paquete import Box


class FincasService:
    """
    Servicio de nivel superior que orquesta operaciones de plantaciones.
    """

    def __init__(self, plantacion_service: PlantacionService, registry: CultivoServiceRegistry):
        self.fincas: List[RegistroForestal] = []
        self.plantacion_service = plantacion_service
        self.registry = registry

    def add_finca(self, finca: RegistroForestal) -> None:
        """Agrega una finca (RegistroForestal) a la lista."""
        self.fincas.append(finca)

    def remover_finca(self, finca: RegistroForestal) -> None:
        """Elimina una finca existente."""
        self.fincas.remove(finca)

    def fumigar(self, id_finca: int, insecticida: str) -> None:
        """Muestra información de fumigación para cada cultivo."""
        print(f"\n[FUMIGACIÓN] Finca {id_finca} con {insecticida}")
        for finca in self.fincas:
            if finca.id_padron == id_finca:
                plantacion = finca.plantacion
                for cultivo in plantacion.cultivos:
                    servicio: CultivoService = self.registry.obtener_servicio(cultivo.__class__.__name__)
                    if servicio:
                        servicio.mostrar_datos(cultivo)

    def regar(self) -> None:
        """Riega todas las fincas registradas."""
        print("\n[RIEGO] Iniciando riego general...")
        for finca in self.fincas:
            self.plantacion_service.regar(finca.plantacion)

    def cosechar_y_empaquetar(self, tipo: Type[Cultivo]) -> Box:
        """
        Cosecha los cultivos de un tipo específico y los empaqueta en una Box<T>.
        """
        print(f"\n[COSECHA] Empaquetando cultivos de tipo {tipo.__name__}")
        box = Box[tipo]()
        for finca in self.fincas:
            for cultivo in finca.plantacion.cultivos:
                if isinstance(cultivo, tipo):
                    box.add_item(cultivo)
        box.mostrar_contenido_caja()
        return box


# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

from typing import Generic, TypeVar, List
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar("T", bound=Cultivo)


class Box(Generic[T]):
    """Contenedor genérico para empaquetar cosechas (bounded generic)."""

    def __init__(self):
        self.items: List[T] = []

    def add_item(self, item: T) -> None:
        """Agrega un cultivo al contenedor."""
        self.items.append(item)

    def get_items(self) -> List[T]:
        """Devuelve la lista de cultivos."""
        return self.items

    def mostrar_contenido_caja(self) -> None:
        """Muestra los cultivos empaquetados."""
        print("\n=== Contenido de la caja ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print("============================\n")


