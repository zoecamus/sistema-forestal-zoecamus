"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================

from typing import NamedTuple

class EventoPlantacion(NamedTuple):
    """Evento emitido cuando ocurre un cambio en la plantación."""
    tipo: str           # 'riego', 'crecimiento', 'consumo', etc.
    mensaje: str        # Descripción legible del evento
    severidad: str      # 'INFO', 'WARNING', 'ERROR'


# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

from typing import NamedTuple

class EventoSensor(NamedTuple):
    """Evento emitido por sensores del sistema de riego."""
    tipo: str           # 'temperatura' o 'humedad'
    valor: float        # Lectura del sensor
    unidad: str         # '°C' o '%'


