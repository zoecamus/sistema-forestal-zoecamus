"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/factory
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoFactory:
    """
    Fábrica centralizada de cultivos.
    Implementa el patrón Factory Method.
    """

    @staticmethod
    def crear_cultivo(tipo: str):
        """
        Crea una instancia del cultivo según el tipo indicado.
        """
        tipo = tipo.lower()
        print(f"Factory: creando cultivo '{tipo}'")

        if tipo == "pino":
            return Pino(variedad="Paraná", altura=45.0, agua=25.0, edad=30, superficie=2.0)
        elif tipo == "olivo":
            return Olivo(tipo_aceituna="Manzanilla", altura=40.0, agua=30.0, edad=25, superficie=1.5)
        elif tipo == "lechuga":
            return Lechuga(agua=10.0, superficie=0.1, edad=45)
        elif tipo == "zanahoria":
            return Zanahoria(tipo="Baby Carrot", agua=8.0, superficie=0.2, edad=45)
        else:
            raise ValueError(f"[ERROR] Tipo de cultivo desconocido: {tipo}")


