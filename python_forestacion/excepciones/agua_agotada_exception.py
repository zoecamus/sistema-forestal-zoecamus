from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Lanzada cuando el agua disponible en la plantación se agota por debajo del mínimo permitido.
    """

    def __init__(self, disponible: int, minima: int):
        super().__init__(
            "ERROR_02",
            f"Agua agotada. Disponible: {disponible} L, mínima requerida: {minima} L."
        )
        self.disponible = disponible
        self.minima = minima
