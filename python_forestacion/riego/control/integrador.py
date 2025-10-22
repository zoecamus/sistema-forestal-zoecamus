"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/control
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_riesgo_task.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/control/control_riesgo_task.py
# ================================================================================

import threading
import time
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class ControlRiegoTask(Observer[EventoSensor], threading.Thread):
    """Controlador que reacciona a los eventos de sensores de temperatura y humedad."""

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self._ejecutando = True
        self._temp_actual: float = 0.0
        self._hum_actual: float = 0.0

    def actualizar(self, evento: EventoSensor) -> None:
        #Reacciona ante cada lectura de los sensores
        if evento.tipo == "temperatura":
            self._temp_actual = evento.valor
        elif evento.tipo == "humedad":
            self._hum_actual = evento.valor

        print(f"[ControlRiego] Recibido evento -> {evento.tipo}: {evento.valor}{evento.unidad}")
        self._evaluar_condiciones()

    def _evaluar_condiciones(self) -> None:
        #Evalúa si deben activarse los sistemas de riego
        if self._temp_actual >= 25.0 and self._hum_actual < 40.0:
            print(" [ControlRiego] Activando riego automático: condiciones secas y calurosas.")
        elif self._hum_actual > 70.0:
            print(" [ControlRiego] Desactivando riego: humedad suficiente.")

    def run(self) -> None:
        #Simula el monitoreo continuo
        print("[ControlRiego] Iniciando sistema de control de riego...")
        while self._ejecutando:
            time.sleep(1)

    def detener(self) -> None:
        #Detiene la ejecución del controlador
        print("[ControlRiego] Deteniendo sistema de control de riego...")
        self._ejecutando = False


