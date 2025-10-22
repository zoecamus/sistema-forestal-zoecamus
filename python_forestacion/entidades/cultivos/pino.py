from python_forestacion.entidades.cultivos.arbol import Arbol

class Pino(Arbol):
    """Representa un árbol de tipo Pino con variedad configurable."""

    def __init__(self, variedad="Paraná", altura=0.0, agua=0.0, superficie=2.0, edad=0):
        super().__init__(altura=altura, agua=agua, superficie=superficie, edad=edad)
        self.variedad = variedad
        self.ciclo_de_vida = 3650  # 10 años

    def tipo(self) -> str:
        return "pino"

    def __str__(self):
        return (f"Pino(variedad={self.variedad}, altura={self.altura}, "
                f"agua={self.agua}, superficie={self.superficie}, "
                f"edad={self.edad}/{self.ciclo_de_vida} días)")
