from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

class Olivo(Arbol):
    """Representa un olivo con tipo de aceituna configurable."""

    def __init__(self, tipo_aceituna=TipoAceituna.ARBEQUINA, altura=0.0, agua=0.0, superficie=1.5, edad=0):
        super().__init__(altura=altura, superficie=superficie, edad=edad)
        if isinstance(tipo_aceituna, str):
            try:
                tipo_aceituna = TipoAceituna[tipo_aceituna.upper()]
            except KeyError:
                tipo_aceituna = TipoAceituna.ARBEQUINA
        self.fruto = tipo_aceituna
        self.ciclo_de_vida = 5475  # 15 años

    def tipo(self) -> str:
        return "Olivo"

    def __str__(self):
        tipo_aceituna = self.fruto.value if hasattr(self.fruto, "value") else self.fruto
        return (f"Olivo(tipo_aceituna={tipo_aceituna}, altura={self.altura}, "
                f"agua={self.agua}, superficie={self.superficie}, "
                f"edad={self.edad}/{self.ciclo_de_vida} días)")
