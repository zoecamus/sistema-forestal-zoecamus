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
