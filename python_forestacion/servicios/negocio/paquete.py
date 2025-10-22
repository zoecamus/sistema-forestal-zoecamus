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
