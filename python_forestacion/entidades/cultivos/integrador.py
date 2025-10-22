"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Enumeración para los tipos de aceituna."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

    def __str__(self):
        return self.value


# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

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


