from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """Servicio para creación y gestión de tierras."""

    def crear_tierra(self, id: int, superficie: float, domicilio: str) -> Tierra:
        """Crea un terreno sin plantación asociada."""
        tierra = Tierra(id=id, superficie=superficie, domicilio=domicilio)
        print(f"[TIERRA] Creada tierra {tierra.id} en {tierra.domicilio} ({tierra.superficie} m²)")
        return tierra

    def crear_tierra_con_plantacion(self, id: int, superficie: float, domicilio: str, nombre_plantacion: str) -> Tierra:
        """Crea una tierra y su plantación asociada."""
        tierra = Tierra(id=id, superficie=superficie, domicilio=domicilio)
        plantacion = Plantacion(id=id, nombre=nombre_plantacion, agua=superficie / 10, tierra=tierra)
        tierra.set_finca(plantacion)
        print(f"[TIERRA] Creada tierra + plantación '{nombre_plantacion}' en {domicilio}")
        return tierra
