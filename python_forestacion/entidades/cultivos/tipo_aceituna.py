from enum import Enum

class TipoAceituna(Enum):
    """Enumeración para los tipos de aceituna."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

    def __str__(self):
        return self.value
