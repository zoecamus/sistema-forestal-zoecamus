from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base para los cultivos tipo Árbol.
    """

    def __init__(self, altura: float = 0.0, agua: float = 0.0, superficie: float = 0.0, edad: float = 0.0):
        super().__init__(superficie=superficie, agua=agua, edad=edad)
        self.altura = altura  # metros de altura del árbol

    def crecer(self, factor: float = 1.0):
        """
        Sobrescribe el crecimiento de los árboles:
        aumentan su altura y edad proporcionalmente.
        """
        self.edad += factor
        self.altura += factor * 0.02  # cada día aumenta 2 cm aprox
        print(f"[ÁRBOL] {self.__class__.__name__} creció a {self.altura:.2f} m (edad: {self.edad}/{self.EDAD_MAXIMA})")

    def __str__(self):
        return (f"{self.__class__.__name__}(altura={self.altura:.2f} m, agua={self.agua:.1f} L, "
                f"superficie={self.superficie:.2f} m², edad={self.edad}/{self.EDAD_MAXIMA})")
