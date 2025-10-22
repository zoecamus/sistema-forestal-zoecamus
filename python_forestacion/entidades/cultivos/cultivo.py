class Cultivo:
    """
    Clase base abstracta para todos los cultivos del sistema forestal.
    Define los atributos y comportamientos comunes.
    """

    EDAD_MAXIMA = 3650  # 10 años por defecto

    def __init__(self, superficie: float = 0.0, agua: float = 0.0, edad: float = 0.0):
        self.superficie = superficie     # m² que ocupa el cultivo
        self.agua = agua                 # litros de agua acumulada
        self.edad = edad                 # edad en días
        self.vivo = True                 # estado del cultivo

    # ------------------------------------------------------------------
    # Métodos genéricos
    # ------------------------------------------------------------------

    def absorber_agua(self, cantidad: float) -> None:
        """Incrementa la cantidad de agua del cultivo."""
        self.agua += cantidad
        print(f"[CULTIVO] {self.__class__.__name__} absorbió {cantidad}L de agua (total: {self.agua}L)")

    def consumir_agua(self, cantidad: float) -> None:
        """Reduce la cantidad de agua del cultivo."""
        if cantidad > self.agua:
            cantidad = self.agua
        self.agua -= cantidad
        print(f"[CULTIVO] {self.__class__.__name__} consumió {cantidad}L de agua (restante: {self.agua}L)")

    def crecer(self, factor: float = 1.0) -> None:
        """
        Simula el crecimiento del cultivo. 
        Las subclases (Arbol, Hortaliza, etc.) pueden sobreescribir este comportamiento.
        """
        self.edad += factor
        if self.edad > self.EDAD_MAXIMA:
            self.edad = self.EDAD_MAXIMA
            self.vivo = False
            print(f"[CULTIVO] {self.__class__.__name__} ha alcanzado su edad máxima y muere.")
        else:
            print(f"[CULTIVO] {self.__class__.__name__} creció {factor} día(s). Edad actual: {self.edad}/{self.EDAD_MAXIMA}")

    def get_superficie(self) -> float:
        return self.superficie

    def get_agua(self) -> float:
        return self.agua

    def set_agua(self, cantidad: float) -> None:
        self.agua = cantidad

    def esta_vivo(self) -> bool:
        return self.vivo

    def __str__(self) -> str:
        return (f"{self.__class__.__name__}(superficie={self.superficie}m², "
                f"agua={self.agua}L, edad={self.edad}/{self.EDAD_MAXIMA})")
