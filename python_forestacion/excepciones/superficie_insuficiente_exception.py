from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Lanzada cuando la superficie disponible de la plantación no alcanza
    para el cultivo solicitado.
    """

    def __init__(self, tipo_cultivo: str, requerida: float, disponible: float):
        super().__init__(
            "ERROR_01",
            f"Superficie insuficiente para {tipo_cultivo}. "
            f"Requerida: {requerida} m², disponible: {disponible} m²."
        )
        self.tipo_cultivo = tipo_cultivo
        self.requerida = requerida
        self.disponible = disponible
