import random
import threading
import time
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class HumedadReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula la lectura de un sensor de humedad cada 3 segundos."""

    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._ultima_humedad: float = 0.0
        self._ejecutando: bool = True

    def run(self) -> None:
        #Ciclo principal del sensor
        print("[SensorHumedad] Iniciando lectura de humedad...")
        while self._ejecutando:
            self._ultima_humedad = self._leer_sensor()
            evento = EventoSensor(tipo="humedad",
                                  valor=self._ultima_humedad,
                                  unidad="%")
            print(f"[SensorHumedad] Nueva lectura: {self._ultima_humedad} %")
            self.notificar_observadores(evento)
            time.sleep(3)

    def _leer_sensor(self) -> float:
        #Devuelve una lectura simulada de humedad
        return round(random.uniform(20.0, 80.0), 2)

    def get_ultima_humedad(self) -> float:
        #Devuelve la última humedad registrada
        return self._ultima_humedad

    def detener(self) -> None:
        #Detiene el ciclo de lectura
        print("[SensorHumedad] Deteniendo lectura de humedad...")
        self._ejecutando = False
