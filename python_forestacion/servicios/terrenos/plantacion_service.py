from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory


class PlantacionService:
    """Servicio que gestiona operaciones de las plantaciones."""

    def __init__(self, registry: CultivoServiceRegistry):
        self.registry = registry

    def crear_plantacion(self, tierra, nombre: str, agua: int) -> Plantacion:
        plantacion = Plantacion(
            id=tierra.id,
            nombre=nombre,
            agua=agua,
            tierra=tierra,
            superficie_total=float(getattr(tierra, "superficie", 0.0))
        )
        print(f"[PLANTACIÓN] Creada '{nombre}' con {agua} L disponibles.")
        return plantacion

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> bool:
        """Agrega nuevos cultivos a la plantación (usa Factory + validaciones)."""
        muestra = CultivoFactory.crear_cultivo(especie)

        sup_por_unidad = float(getattr(muestra, "superficie", 0.0))
        cant = int(cantidad)
        sup_necesaria = sup_por_unidad * cant

        sup_disp = float(plantacion.superficie_disponible)

        if sup_disp < sup_necesaria:
            raise SuperficieInsuficienteException(
                especie, sup_necesaria, sup_disp
            )

        for _ in range(cant):
            plantacion.agregar_cultivo(CultivoFactory.crear_cultivo(especie))
            print(f" Plantado {especie} en '{plantacion.nombre}'")

        return True

    def regar(self, plantacion: Plantacion) -> bool:
        if float(plantacion.agua_disponible) < 10.0:
            raise AguaAgotadaException(plantacion.agua_disponible, 10)

        print(f"[RIEGO] Regando '{plantacion.nombre}' con {plantacion.agua_disponible} L disponibles...")
        for cultivo in plantacion.cultivos:
            servicio = self.registry.obtener_servicio(cultivo.__class__.__name__)
            if servicio:
                agua = servicio.absorver_agua(cultivo)
                cultivo.agua = float(cultivo.agua) + float(agua)
                plantacion.agua_disponible = float(plantacion.agua_disponible) - float(agua)
        return True
