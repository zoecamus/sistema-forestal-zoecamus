from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """
    Representa una zanahoria cultivada.
    Puede ser normal o tipo 'Baby Carrot'.
    """

    def __init__(self, tipo="Baby Carrot", agua=8.0, superficie=0.2, edad=0.0):
        super().__init__(agua=agua, superficie=superficie, invernadero=False, edad=edad)
        self.tipo = tipo
        self.ciclo_de_vida = 120  # 4 meses promedio

    def tipo_cultivo(self):
        return "Zanahoria"

    def __str__(self):
        return (f"Zanahoria(tipo={self.tipo}, agua={self.agua} L, "
                f"superficie={self.superficie} m², edad={self.edad}/{self.ciclo_de_vida} días)")
