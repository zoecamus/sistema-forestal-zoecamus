from typing import NamedTuple

class EventoPlantacion(NamedTuple):
    """Evento emitido cuando ocurre un cambio en la plantación."""
    tipo: str           # 'riego', 'crecimiento', 'consumo', etc.
    mensaje: str        # Descripción legible del evento
    severidad: str      # 'INFO', 'WARNING', 'ERROR'
