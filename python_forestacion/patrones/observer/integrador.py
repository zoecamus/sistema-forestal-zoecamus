"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/observer.py
# ================================================================================

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


