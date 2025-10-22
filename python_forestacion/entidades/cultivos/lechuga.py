from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

class Lechuga(Hortaliza):
    """Representa una lechuga cultivada, generalmente de invernadero."""

    def __init__(self, agua=10, superficie=0.1, edad=0, invernadero=True):
        super().__init__(agua=agua, superficie=superficie, invernadero=invernadero, edad=edad)
        self.ciclo_de_vida = 90  # días promedio

    def tipo(self):
        return "Lechuga"

    def __str__(self):
        tipo = "Sí" if self.requiere_invernadero else "No"
        return f"Lechuga(invernadero={tipo}, agua={self.agua}L, edad={self.edad}/{self.ciclo_de_vida} días)"
