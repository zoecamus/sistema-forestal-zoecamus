from typing import Generic, Protocol, TypeVar

T = TypeVar("T")

class Observer(Protocol, Generic[T]):
    """Interfaz genérica del patrón Observer.

    Define el método que los observadores deben implementar para reaccionar
    ante notificaciones del objeto observable.
    """

    def actualizar(self, evento: T) -> None:
        """Se ejecuta cuando el observable emite un evento.

        Args:
            evento: Información o estado emitido por el observable.
        """
        ...
