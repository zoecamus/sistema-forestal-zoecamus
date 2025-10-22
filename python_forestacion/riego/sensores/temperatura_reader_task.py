import random
import threading
import time
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class TemperaturaReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula la lectura de un sensor de temperatura cada 2 segundos."""

    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._ultima_temperatura: float = 0.0
        self._ejecutando: bool = True

    def run(self) -> None:
        #Ciclo principal del sensor
        print("[SensorTemperatura] Iniciando lectura de temperatura...")
        while self._ejecutando:
            self._ultima_temperatura = self._leer_sensor()
            evento = EventoSensor(tipo="temperatura",
                                  valor=self._ultima_temperatura,
                                  unidad="°C")
            print(f"[SensorTemperatura] Nueva lectura: {self._ultima_temperatura} °C")
            self.notificar_observadores(evento)
            time.sleep(2)

    def _leer_sensor(self) -> float:
        #Devuelve una lectura simulada de temperatura
        return round(random.uniform(10.0, 30.0), 2)

    def get_ultima_temperatura(self) -> float:
        #Devuelve la última temperatura registrada
        return self._ultima_temperatura

    def detener(self) -> None:
        #Detiene el ciclo de lectura
        print("[SensorTemperatura] Deteniendo lectura de temperatura...")
        self._ejecutando = False
