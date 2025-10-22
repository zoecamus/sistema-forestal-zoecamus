from __future__ import annotations
from threading import Lock
from typing import Generic, List, TypeVar
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

class Observable(Generic[T]):
    """Clase base para objetos observables.

    Mantiene una lista de observadores y los notifica cuando ocurre un cambio.
    Implementa sincronización por Lock para garantizar thread-safety.
    """

    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []
        self._lock = Lock()

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador al listado.

        Args:
            observador: Instancia que implementa la interfaz Observer.
        """
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador del listado.

        Args:
            observador: Instancia previamente registrada.
        """
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados.

        Args:
            evento: Información o estado a propagar a los observadores.
        """
        with self._lock:
            for obs in self._observadores:
                obs.actualizar(evento)
