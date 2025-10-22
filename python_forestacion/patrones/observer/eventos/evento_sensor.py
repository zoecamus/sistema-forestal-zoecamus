from typing import NamedTuple

class EventoSensor(NamedTuple):
    """Evento emitido por sensores del sistema de riego."""
    tipo: str           # 'temperatura' o 'humedad'
    valor: float        # Lectura del sensor
    unidad: str         # '°C' o '%'
