from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base para todas las hortalizas del sistema."""

    def __init__(self, agua: int, superficie: float, invernadero: bool, edad=0):
        super().__init__(superficie=superficie, agua=agua, edad=edad)
        self.requiere_invernadero = invernadero
        self.ciclo_de_vida = 120  # promedio

    def crecer(self, factor=1.0):
        """Simula el crecimiento de la hortaliza según el agua o estación."""
        self.edad += factor
        if self.edad > self.ciclo_de_vida:
            self.edad = self.ciclo_de_vida
        print(f"[HORTALIZA] {self.__class__.__name__} creció {factor:.1f} día(s) "
              f"(edad: {self.edad}/{self.ciclo_de_vida})")

    def absorber_agua(self, cantidad: int):
        self.agua += cantidad

    def tipo(self) -> str:
        return "hortaliza"

    def __str__(self):
        inv = "Sí" if self.requiere_invernadero else "No"
        return (f"{self.__class__.__name__}(invernadero={inv}, agua={self.agua}L, "
                f"superficie={self.superficie}m², edad={self.edad}/{self.ciclo_de_vida} días)")
