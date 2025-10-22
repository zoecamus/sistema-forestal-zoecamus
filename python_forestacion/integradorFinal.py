"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion
Fecha de generacion: 2025-10-22 09:45:41
Total de archivos integrados: 68
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================
#
# DRECTORIO: ..
#   1. main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones/factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   38. __init__.py
#   39. singleton.py
#
# DIRECTORIO: patrones/strategy
#   40. __init__.py
#   41. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   42. __init__.py
#   43. absorcion_constante_strategy.py
#   44. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   45. __init__.py
#
# DIRECTORIO: riego/control
#   46. __init__.py
#   47. control_riesgo_task.py
#
# DIRECTORIO: riego/sensores
#   48. __init__.py
#   49. humedad_reader_task.py
#   50. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   51. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   52. __init__.py
#   53. arbol_service.py
#   54. cultivo_service.py
#   55. cultivo_service_registry.py
#   56. lechuga_service.py
#   57. olivo_service.py
#   58. pino_service.py
#   59. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   60. __init__.py
#   61. fincas_service.py
#   62. paquete.py
#
# DIRECTORIO: servicios/personal
#   63. __init__.py
#   64. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   65. __init__.py
#   66. plantacion_service.py
#   67. registro_forestal_services.py
#   68. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/68: main.py
# Directorio: ..
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/main.py
# ==============================================================================

# ================================================================
# SISTEMA DE GESTION FORESTAL - PATRONES DE DISEÑO
# ================================================================

from datetime import date
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.personal.trabajador import Trabajador, PropietarioFinca, AuditorInspector
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.registro_forestal_services import RegistroForestalService
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import CONFIG_CULTIVOS
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

# ===============================================================
#  FUNCIÓN: RESUMEN FINAL DE LA SIMULACIÓN
# ===============================================================
def mostrar_resumen_final(plantacion):
    print("\n" + "=" * 70)
    print("                      RESUMEN FINAL DE LA SIMULACIÓN")
    print("=" * 70)
    print(f" Finca: {plantacion.nombre}")
    print(f" Ubicación: {plantacion.tierra.domicilio if plantacion.tierra else 'Desconocida'}")
    print(f" Agua disponible final: {plantacion.agua_disponible:.2f} L")
    print(f" Superficie total: {plantacion.superficie_total:.2f} m²")
    print(f" Superficie ocupada: {plantacion.superficie_ocupada:.2f} m²")
    print(f" Superficie libre: {plantacion.superficie_disponible:.2f} m²")
    print("\n=== Cultivos en la finca ===")

    if not plantacion.cultivos:
        print("   (No hay cultivos registrados)")
    else:
        tipos = {}
        for c in plantacion.cultivos:
            nombre = c.__class__.__name__
            tipos[nombre] = tipos.get(nombre, 0) + 1
        for tipo, cantidad in tipos.items():
            print(f"   - {tipo}: {cantidad}")
    print("=" * 70 + "\n")


# ===============================================================
#  DEMOSTRACIÓN PRINCIPAL
# ===============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("        SISTEMA DE GESTION FORESTAL - PATRONES DE DISEÑO  ")
    print("=" * 70)

    # -----------------------------------------------------------
    # PATRÓN SINGLETON
    # -----------------------------------------------------------
    print("\n----------------------------------------------------------------------")
    print("   PATRÓN SINGLETON: Inicializando servicios")
    print("----------------------------------------------------------------------")

    registry1 = CultivoServiceRegistry()
    registry2 = CultivoServiceRegistry()
    print(f"ID de instancia: {id(registry1)}")

    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry ")
    else:
        print("[ERROR] Las instancias del Registry no coinciden ")

    # -----------------------------------------------------------
    # CREACIÓN DE TIERRA Y PLANTACIÓN
    # -----------------------------------------------------------
    print("\n----------------------------------------------------------------------")
    print("   CREACIÓN DE TIERRA Y PLANTACIÓN")
    print("----------------------------------------------------------------------")

    tierra = Tierra(id=1, superficie=20000.0, domicilio="Agrelo")
    print(f"[TIERRA] Creada tierra Padrón #{tierra.id} en {tierra.domicilio} ({tierra.superficie} m²)")

    plant_serv = PlantacionService(registry1)
    plantacion = plant_serv.crear_plantacion(tierra, "Finca Zoe", agua=8000)
    tierra.set_finca(plantacion)
    print(f"[PLANTACIÓN] Creada '{plantacion.nombre}' con {plantacion.agua_disponible} L disponibles.")
    print(" Plantación creada exitosamente.\n")

    # -----------------------------------------------------------
    # FACTORY METHOD
    # -----------------------------------------------------------
    print("----------------------------------------------------------------------")
    print("   PATRÓN FACTORY METHOD: Creación de cultivos")
    print("----------------------------------------------------------------------")

    especies = ["pino", "olivo", "lechuga", "zanahoria"]
    cultivos = [CultivoFactory.crear_cultivo(e) for e in especies]

    for cultivo in cultivos:
        cultivo.crecer(45)

    for c in cultivos:
        print(f" - Se creó: {c}")
    print(" Factory probado correctamente.\n")

    # -----------------------------------------------------------
    # PERSONAL Y SERVICIOS
    # -----------------------------------------------------------
    print("----------------------------------------------------------------------")
    print("   GESTIÓN DE PERSONAL Y TAREAS")
    print("----------------------------------------------------------------------")

    tareas = [
        Tarea(1, "Cosechar lechugas", date.today()),
        Tarea(2, "Controlar humedad del suelo", date.today()),
    ]
    trabajador = Trabajador(43888734, "Juan Pérez", tareas)
    herramienta = Herramienta(1, "Pala", True)

    servicio_trabajador = TrabajadorService()
    servicio_trabajador.asignar_apto_medico(trabajador, True, date.today(), "Apto general")
    servicio_trabajador.trabajar(trabajador, date.today(), herramienta)

    propietario = PropietarioFinca("Zoe Camus", 50309233)
    propietario.supervisar_operaciones()
    propietario.registrar_finca("Finca Zoe")

    auditor = AuditorInspector("Inspector Forestal Mendoza")
    auditor.verificar_registro("Zoe Camus")

    print(" Personal y actores del sistema probados correctamente.\n")

    # -----------------------------------------------------------
    # ESTRATEGIAS DE ABSORCIÓN (STRATEGY)
    # -----------------------------------------------------------
    print("----------------------------------------------------------------------")
    print("   PATRÓN STRATEGY: Simulación de absorción de agua")
    print("----------------------------------------------------------------------")

    try:
        # Poblar la finca automáticamente según CONFIG_CULTIVOS
        for _ in range(CONFIG_CULTIVOS.get("pino", 0)):
            plant_serv.plantar(plantacion, "pino", 1)
        for _ in range(CONFIG_CULTIVOS.get("olivo", 0)):
            plant_serv.plantar(plantacion, "olivo", 1)
        for _ in range(CONFIG_CULTIVOS.get("lechuga", 0)):
            plant_serv.plantar(plantacion, "lechuga", 1)
        for _ in range(CONFIG_CULTIVOS.get("zanahoria", 0)):
            plant_serv.plantar(plantacion, "zanahoria", 1)
    except Exception as e:
        print(f"[ADVERTENCIA] {e}")

    mostrar_resumen_final(plantacion)

    # -----------------------------------------------------------
    # REGISTRO FORESTAL Y AVALÚO FISCAL
    # -----------------------------------------------------------
    print("\n----------------------------------------------------------------------")
    print("   REGISTRO FORESTAL Y AVALUO FISCAL")
    print("----------------------------------------------------------------------")

    try:
        plantacion.set_trabajadores([trabajador])
        registry = CultivoServiceRegistry()
        reg_serv = RegistroForestalService(registry)
        registro = RegistroForestal(
            id_padron=1,
            tierra=tierra,
            plantacion=plantacion,
            propietario="Zoe Camus",
            avaluo=50309233.55
        )
        reg_serv.persistir(registro)
        print("[PERSISTENCIA] Registro 'Zoe Camus' guardado en data/Zoe Camus.dat")
        print("[OK] Registro guardado exitosamente.\n")
        reg_serv.mostrar_datos(registro)
    except Exception as e:
        print(f"[ERROR] No se pudo crear el registro forestal: {e}")

    # -----------------------------------------------------------
    # CIERRE FINAL
    # -----------------------------------------------------------
    print("=" * 70)
    print("         EJEMPLO COMPLETADO EXITOSAMENTE ")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia única)")
    print("  [OK] FACTORY     - Creación de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorción de agua")
    print("=" * 70)


# ==============================================================================
# ARCHIVO 2/68: __init__.py
# Directorio: .
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/68: constantes.py
# Directorio: .
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/constantes.py
# ==============================================================================

"""
Módulo de constantes globales del sistema de gestión forestal.

Centraliza valores numéricos y configuraciones usadas en todo el proyecto.
Cumple con el principio DRY y evita el uso de "magic numbers".
"""

# ============================================================
#  CONSTANTES DE CULTIVOS
# ============================================================

# Pino
SUPERFICIE_PINO = 2.0             # m²
AGUA_INICIAL_PINO = 25             # litros
ALTURA_INICIAL_PINO = 1.5         # metros

# Olivo
SUPERFICIE_OLIVO = 3.0            # m²
AGUA_INICIAL_OLIVO = 30            # litros
ALTURA_INICIAL_OLIVO = 1        # metros

# Lechuga
SUPERFICIE_LECHUGA = 0.10         # m²
AGUA_INICIAL_LECHUGA = 10          # litros

# Zanahoria
SUPERFICIE_ZANAHORIA = 0.15       # m²
AGUA_INICIAL_ZANAHORIA = 8        # litros


# ============================================================
#  CONSTANTES DE RIEGO Y ESTRATEGIAS
# ============================================================

# Absorción estacional (Strategy)
ABSORCION_SEASONAL_VERANO = 5     # L
ABSORCION_SEASONAL_INVIERNO = 2   # L

# Absorción constante (Strategy)
ABSORCION_CONST_LECHUGA = 1       # L
ABSORCION_CONST_ZANAHORIA = 2     # L

# Estaciones (para absorber agua según mes)
MES_INICIO_VERANO = 3             # Marzo
MES_FIN_VERANO = 8                # Agosto


# ============================================================
#  CONSTANTES DE SENSORES (Observer)
# ============================================================

INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25               # °C
SENSOR_TEMP_MAX = 50                # °C

INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
SENSOR_HUMEDAD_MIN = 0              # %
SENSOR_HUMEDAD_MAX = 100            # %

TEMP_MIN_RIEGO = 8                  # °C
TEMP_MAX_RIEGO = 15                 # °C
HUMEDAD_MAX_RIEGO = 50              # %
INTERVALO_CONTROL_RIEGO = 2.5       # segundos

THREAD_JOIN_TIMEOUT = 2.0           # segundos


# ============================================================
#  CONSTANTES DE PERSISTENCIA
# ============================================================

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
AGUA_CONSUMO_RIEGO = 10             # litros por riego


# ============================================================
#  OTROS
# ============================================================

AGUA_INICIAL_PLANTACION = 1000       # litros
VERSION_SISTEMA = "1.0.0"


# ==========================================================
# CONFIGURACIÓN DE SIMULACIÓN (cantidad inicial de cultivos)
# ==========================================================

CONFIG_CULTIVOS = {
    "pino": 5,
    "olivo": 4,
    "lechuga": 10,
    "zanahoria": 15
}




################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/68: __init__.py
# Directorio: entidades
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/68: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/68: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 7/68: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 8/68: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 9/68: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 10/68: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 11/68: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 12/68: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Enumeración para los tipos de aceituna."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

    def __str__(self):
        return self.value


# ==============================================================================
# ARCHIVO 13/68: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 14/68: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/68: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

from dataclasses import dataclass
from datetime import date

@dataclass
class AptoMedico:
    """Certifica si un trabajador está apto para trabajar."""
    apto: bool
    fecha_emision: date
    observaciones: str

    def esta_apto(self) -> bool:
        return self.apto

    def get_resumen(self) -> str:
        estado = "APTO" if self.apto else "NO APTO"
        return f"AptoMedico({estado}, emitido={self.fecha_emision}, obs='{self.observaciones}')"

    def __str__(self):
        return self.get_resumen()


# ==============================================================================
# ARCHIVO 16/68: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class Herramienta:
    """Representa una herramienta utilizada por los trabajadores."""

    id: int
    nombre: str
    estado: str = "Operativa" 
    certificacion_seguridad: str = "IRAM-ISO 45001" #norma argentina e internacional sobre seguridad laboral

    def get_nombre(self):
        return self.nombre
    
    def __str__(self):
        return (f"Herramienta(id={self.id}, nombre='{self.nombre}', estado={self.estado}, "
                f"certificación={self.certificacion_seguridad})")





# ==============================================================================
# ARCHIVO 17/68: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from datetime import date

class Tarea:
    """Representa una tarea asignada a un trabajador."""

    def __init__(self, id: int, descripcion: str, fecha_programada: date):
        self.id = id
        self.descripcion = descripcion
        self.fecha_programada = fecha_programada
        self.completada = False  # estado inicial

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __repr__(self):
        estado = "COMPLETADA" if self.completada else "PENDIENTE"
        return f"Tarea(id={self.id}, desc='{self.descripcion}', fecha={self.fecha_programada}, estado={estado})"
    
    @property
    def estado(self):
        return self.completada

# ==============================================================================
# ARCHIVO 18/68: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from datetime import date
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    """
    Representa a un trabajador agrícola, con DNI, nombre, apto médico y tareas asignadas.
    """

    def __init__(self, dni: int, nombre: str, tareas=None):
        self.dni = dni
        self.nombre = nombre
        self.apto_medico = None
        self.tareas = tareas or []

    def get_nombre(self):
        return self.nombre

    def get_apto_medico(self):
        return self.apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico):
        #Asigna o actualiza el apto médico del trabajador
        self.apto_medico = apto_medico

    def get_tareas(self):
        return list(self.tareas)

    def asignar_apto_medico(self, apto: bool, fecha: date, obs: str):
        #Crea y asigna un nuevo AptoMedico
        self.apto_medico = AptoMedico(apto, fecha, obs)

    def __repr__(self):
        return f"Trabajador(dni={self.dni}, nombre='{self.nombre}')"

class PropietarioFinca:
    """Actor del sistema: gestiona el registro forestal y supervisa operaciones."""

    def __init__(self, nombre: str, dni: int):
        self.nombre = nombre
        self.dni = dni

    def supervisar_operaciones(self):
        print(f"[PROPIETARIO] {self.nombre} supervisa las operaciones de la finca.")

    def registrar_finca(self, nombre_finca: str):
        print(f"[PROPIETARIO] {self.nombre} registró la finca '{nombre_finca}' exitosamente.")


class AuditorInspector:
    """Actor del sistema: consulta registros persistidos para verificación."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    def verificar_registro(self, propietario: str):
        print(f"[AUDITOR] {self.nombre} está verificando el registro de '{propietario}' en el sistema.")




################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/68: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/68: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.cultivos.cultivo import Cultivo



class Plantacion:
    """
    Representa una plantación agrícola con cultivos y trabajadores.
    """
    def __init__(self, id: int, nombre: str, agua: int, tierra: Tierra, superficie_total: float = None):
        self.id = id
        self.nombre = nombre
        self.agua_disponible = agua
        self.tierra = tierra                  
        self.situada_en = tierra             
        self.cultivos = []
        self.trabajadores = []
        self.superficie_total = superficie_total if superficie_total is not None else getattr(tierra, "superficie", 0.0)


    @property
    def superficie_ocupada(self) -> float:
        return sum(getattr(c, "superficie", 0.0) for c in self.cultivos)

    @property
    def superficie_disponible(self) -> float:
        return self.superficie_total - self.superficie_ocupada

    def __str__(self):
        return (f"Plantacion(id={self.id}, nombre='{self.nombre}', "
                f"superficie_total={self.superficie_total}, "
                f"ocupada={self.superficie_ocupada:.2f}, "
                f"agua={self.agua_disponible})")

    def get_cultivos(self):
        return list(self.cultivos)

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def get_cultivos_interno(self):
        return self.cultivos

    def get_trabajadores(self):
        return list(self.trabajadores)

    def get_trabajadores_interno(self):
        return self.trabajadores

    def set_trabajadores(self, trabajadores):
        self.trabajadores = trabajadores

    def get_tierra(self):
        return self.situada_en

    def get_agua_disponible(self):
        return self.agua_disponible

    def set_agua_disponible(self, cantidad):
        self.agua_disponible = cantidad

    def __repr__(self):
        return f"Plantacion(id={self.id}, nombre='{self.nombre}', agua={self.agua_disponible})"


# ==============================================================================
# ARCHIVO 21/68: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class RegistroForestal:
    """Registro administrativo y económico de una finca."""
    id_padron: int
    tierra: Tierra
    plantacion: Plantacion
    propietario: str
    avaluo: float


    def __post_init__(self):
        """Validación automática tras la creación del dataclass."""
        if self.avaluo <= 0:
            raise ValueError("El avalúo fiscal debe ser mayor a 0.")

    def __str__(self):
        return (
            f"RegistroForestal(id_padron={self.id_padron}, "
            f"propietario='{self.propietario}', "
            f"avaluo=${self.avaluo:,.2f}, "
            f"plantacion='{self.plantacion.nombre}')"
        )


# ==============================================================================
# ARCHIVO 22/68: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

@dataclass
class Tierra:
    """Representa un terreno físico donde se puede ubicar una plantación."""
    id: int
    superficie: float
    domicilio: str
    finca: Optional["Plantacion"] = None  

    # Métodos
    def set_finca(self, finca: "Plantacion"):
        self.finca = finca

    def get_finca(self):
        return self.finca

    def __str__(self):
        return f"Tierra(id={self.id}, superficie={self.superficie}, domicilio='{self.domicilio}')"
   
    def __repr__(self):
        return f"Tierra(Padrón #{self.id}, Superficie={self.superficie} m², Domicilio='{self.domicilio}')"

    def get_id(self):
        return self.id




################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/68: __init__.py
# Directorio: excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/68: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 25/68: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del sistema de forestación.
    """

    def __init__(self, error_code: str, user_message: str):
        super().__init__(f"[{error_code}] {user_message}")
        self.error_code = error_code
        self.user_message = user_message

    def get_error_code(self):
        return self.error_code

    def get_user_message(self):
        return self.user_message

    def get_full_message(self):
        return f"Error {self.error_code}: {self.user_message}"


# ==============================================================================
# ARCHIVO 26/68: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

class MensajesException:
    """
    Centraliza los mensajes de error del sistema para mantener coherencia.
    """

    SUPERFICIE_INSUFICIENTE = "Superficie insuficiente para el cultivo solicitado."
    AGUA_AGOTADA = "El nivel de agua en la plantación es insuficiente."
    PERSISTENCIA_ERROR = "Error durante la persistencia de datos."
    REGISTRO_NO_ENCONTRADO = "No se encontró el registro solicitado."


# ==============================================================================
# ARCHIVO 27/68: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepción para errores de lectura/escritura de archivos de persistencia.
    """

    def __init__(self, tipo_operacion: str, nombre_archivo: str):
        super().__init__(
            "ERROR_03",
            f"Error en operación de {tipo_operacion} sobre archivo '{nombre_archivo}'."
        )
        self.tipo_operacion = tipo_operacion
        self.nombre_archivo = nombre_archivo

    @staticmethod
    def from_ioerror(nombre_archivo: str):
        return PersistenciaException("ESCRITURA", nombre_archivo)

    @staticmethod
    def from_classnotfound(nombre_archivo: str):
        return PersistenciaException("LECTURA", nombre_archivo)


# ==============================================================================
# ARCHIVO 28/68: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/68: __init__.py
# Directorio: patrones
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 30/68: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/68: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 32/68: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/68: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from __future__ import annotations
from threading import Lock
from typing import Generic, List, TypeVar
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

class Observable(Generic[T]):
    """Clase base para objetos observables.

    Mantiene una lista de observadores y los notifica cuando ocurre un cambio.
    Implementa sincronización por Lock para garantizar thread-safety.
    """

    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []
        self._lock = Lock()

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador al listado.

        Args:
            observador: Instancia que implementa la interfaz Observer.
        """
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador del listado.

        Args:
            observador: Instancia previamente registrada.
        """
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados.

        Args:
            evento: Información o estado a propagar a los observadores.
        """
        with self._lock:
            for obs in self._observadores:
                obs.actualizar(evento)


# ==============================================================================
# ARCHIVO 34/68: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from typing import Generic, Protocol, TypeVar

T = TypeVar("T")

class Observer(Protocol, Generic[T]):
    """Interfaz genérica del patrón Observer.

    Define el método que los observadores deben implementar para reaccionar
    ante notificaciones del objeto observable.
    """

    def actualizar(self, evento: T) -> None:
        """Se ejecuta cuando el observable emite un evento.

        Args:
            evento: Información o estado emitido por el observable.
        """
        ...



################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/68: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/68: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================

from typing import NamedTuple

class EventoPlantacion(NamedTuple):
    """Evento emitido cuando ocurre un cambio en la plantación."""
    tipo: str           # 'riego', 'crecimiento', 'consumo', etc.
    mensaje: str        # Descripción legible del evento
    severidad: str      # 'INFO', 'WARNING', 'ERROR'


# ==============================================================================
# ARCHIVO 37/68: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

from typing import NamedTuple

class EventoSensor(NamedTuple):
    """Evento emitido por sensores del sistema de riego."""
    tipo: str           # 'temperatura' o 'humedad'
    valor: float        # Lectura del sensor
    unidad: str         # '°C' o '%'



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/68: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/68: singleton.py
# Directorio: patrones/singleton
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/singleton/singleton.py
# ==============================================================================

from threading import Lock

class SingletonMeta(type):
    """Metaclase Singleton: garantiza una única instancia."""
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 40/68: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/68: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Protocol

class AbsorcionAguaStrategy(ABC):
    """Interfaz base del patrón Strategy para definir cómo los cultivos absorben agua."""

    @abstractmethod
    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        #Calcula la cantidad de agua a absorber según condiciones ambientales
        pass



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 42/68: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/68: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_CONST_LECHUGA,
    ABSORCION_CONST_ZANAHORIA,
)

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción constante (para hortalizas)."""

    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        if tipo_cultivo.lower() == "lechuga":
            return ABSORCION_CONST_LECHUGA
        elif tipo_cultivo.lower() == "zanahoria":
            return ABSORCION_CONST_ZANAHORIA
        else:
            return 1.5  


# ==============================================================================
# ARCHIVO 44/68: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
)

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción estacional (para árboles)."""

    def calcular_absorcion(self, tipo_cultivo: str, temperatura: float, humedad: float) -> float:
        mes = date.today().month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO  # verano
        else:
            return ABSORCION_SEASONAL_INVIERNO  # invierno



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 45/68: __init__.py
# Directorio: riego
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 46/68: __init__.py
# Directorio: riego/control
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/68: control_riesgo_task.py
# Directorio: riego/control
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/control/control_riesgo_task.py
# ==============================================================================

import threading
import time
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class ControlRiegoTask(Observer[EventoSensor], threading.Thread):
    """Controlador que reacciona a los eventos de sensores de temperatura y humedad."""

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self._ejecutando = True
        self._temp_actual: float = 0.0
        self._hum_actual: float = 0.0

    def actualizar(self, evento: EventoSensor) -> None:
        #Reacciona ante cada lectura de los sensores
        if evento.tipo == "temperatura":
            self._temp_actual = evento.valor
        elif evento.tipo == "humedad":
            self._hum_actual = evento.valor

        print(f"[ControlRiego] Recibido evento -> {evento.tipo}: {evento.valor}{evento.unidad}")
        self._evaluar_condiciones()

    def _evaluar_condiciones(self) -> None:
        #Evalúa si deben activarse los sistemas de riego
        if self._temp_actual >= 25.0 and self._hum_actual < 40.0:
            print(" [ControlRiego] Activando riego automático: condiciones secas y calurosas.")
        elif self._hum_actual > 70.0:
            print(" [ControlRiego] Desactivando riego: humedad suficiente.")

    def run(self) -> None:
        #Simula el monitoreo continuo
        print("[ControlRiego] Iniciando sistema de control de riego...")
        while self._ejecutando:
            time.sleep(1)

    def detener(self) -> None:
        #Detiene la ejecución del controlador
        print("[ControlRiego] Deteniendo sistema de control de riego...")
        self._ejecutando = False



################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 48/68: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 49/68: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import random
import threading
import time
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class HumedadReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula la lectura de un sensor de humedad cada 3 segundos."""

    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._ultima_humedad: float = 0.0
        self._ejecutando: bool = True

    def run(self) -> None:
        #Ciclo principal del sensor
        print("[SensorHumedad] Iniciando lectura de humedad...")
        while self._ejecutando:
            self._ultima_humedad = self._leer_sensor()
            evento = EventoSensor(tipo="humedad",
                                  valor=self._ultima_humedad,
                                  unidad="%")
            print(f"[SensorHumedad] Nueva lectura: {self._ultima_humedad} %")
            self.notificar_observadores(evento)
            time.sleep(3)

    def _leer_sensor(self) -> float:
        #Devuelve una lectura simulada de humedad
        return round(random.uniform(20.0, 80.0), 2)

    def get_ultima_humedad(self) -> float:
        #Devuelve la última humedad registrada
        return self._ultima_humedad

    def detener(self) -> None:
        #Detiene el ciclo de lectura
        print("[SensorHumedad] Deteniendo lectura de humedad...")
        self._ejecutando = False


# ==============================================================================
# ARCHIVO 50/68: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import random
import threading
import time
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class TemperaturaReaderTask(Observable[EventoSensor], threading.Thread):
    """Simula la lectura de un sensor de temperatura cada 2 segundos."""

    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self._ultima_temperatura: float = 0.0
        self._ejecutando: bool = True

    def run(self) -> None:
        #Ciclo principal del sensor
        print("[SensorTemperatura] Iniciando lectura de temperatura...")
        while self._ejecutando:
            self._ultima_temperatura = self._leer_sensor()
            evento = EventoSensor(tipo="temperatura",
                                  valor=self._ultima_temperatura,
                                  unidad="°C")
            print(f"[SensorTemperatura] Nueva lectura: {self._ultima_temperatura} °C")
            self.notificar_observadores(evento)
            time.sleep(2)

    def _leer_sensor(self) -> float:
        #Devuelve una lectura simulada de temperatura
        return round(random.uniform(10.0, 30.0), 2)

    def get_ultima_temperatura(self) -> float:
        #Devuelve la última temperatura registrada
        return self._ultima_temperatura

    def detener(self) -> None:
        #Detiene el ciclo de lectura
        print("[SensorTemperatura] Deteniendo lectura de temperatura...")
        self._ejecutando = False



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 51/68: __init__.py
# Directorio: servicios
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 52/68: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 53/68: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class ArbolService(CultivoService, ABC):
    """Servicio base para árboles."""

    @abstractmethod
    def crecer(self, arbol: Arbol, incremento: float) -> None:
        """Simula el crecimiento de un árbol."""
        pass


# ==============================================================================
# ARCHIVO 54/68: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from abc import ABC, abstractmethod
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """Servicio base para cualquier tipo de cultivo."""

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra información general del cultivo."""
        pass


# ==============================================================================
# ARCHIVO 55/68: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from python_forestacion.patrones.singleton.singleton import SingletonMeta
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy



class CultivoServiceRegistry(metaclass=SingletonMeta):
    """Centraliza los servicios de cultivos (patrón Registry + Singleton)."""

    def __init__(self):
        """Inicializa los servicios solo una vez (gracias al Singleton)."""
        # Verifica si ya fueron cargados
        if not hasattr(self, "_handlers"):
            self._handlers = {
                "Pino": PinoService(AbsorcionConstanteStrategy()),
                "Olivo": OlivoService(AbsorcionSeasonalStrategy()),
                "Lechuga": LechugaService(AbsorcionConstanteStrategy()),
                "Zanahoria": ZanahoriaService(AbsorcionConstanteStrategy()),
            }

    def obtener_servicio(self, nombre: str):
        """Devuelve el servicio correspondiente a un cultivo."""
        return self._handlers.get(nombre)

    def mostrar_servicios(self):
        print("\n=== Servicios registrados ===")
        for nombre, servicio in self._handlers.items():
            print(f"- {nombre}: {servicio.__class__.__name__}")


# ==============================================================================
# ARCHIVO 56/68: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================
import random
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class LechugaService(CultivoService):
    """Servicio para operaciones sobre el cultivo Lechuga."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, lechuga: Lechuga) -> int:
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[LechugaService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(lechuga, temperatura, humedad)

    def mostrar_datos(self, lechuga: Lechuga):
        print(f"[LECHUGA] Variedad: {lechuga.variedad} | Agua: {lechuga.agua}L | "
                f"Invernadero: {lechuga.invernadero} | Edad: {lechuga.edad}/{lechuga.ciclo_de_vida} días")


# ==============================================================================
# ARCHIVO 57/68: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

import random
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class OlivoService(ArbolService):
    """Servicio para operaciones sobre el cultivo Olivo."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, olivo: Olivo) -> int:
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[OlivoService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(olivo, temperatura, humedad)

    def crecer(self, arbol: Olivo, incremento: float) -> None:
        arbol.altura += incremento


    def mostrar_datos(self, olivo: Olivo):
        print(f"[OLIVO] Tipo de aceituna: {olivo.fruto.name} | Altura: {olivo.altura}m | "
                f"Agua: {olivo.agua}L | Edad: {olivo.edad}/{olivo.ciclo_de_vida} días")



# ==============================================================================
# ARCHIVO 58/68: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

import random
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class PinoService(ArbolService):
    """Servicio para operaciones sobre el cultivo Pino."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, pino: Pino) -> int:
        """Aplica la estrategia de absorción de agua con condiciones simuladas."""
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[PinoService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(pino, temperatura, humedad)

    def crecer(self, arbol: Pino, incremento: float) -> None:
        arbol.altura += incremento

    def mostrar_datos(self, pino: Pino):
        print(f"[PINO] Variedad: {pino.variedad} | Altura: {pino.altura}m | "
                f"Agua: {pino.agua}L | Edad: {pino.edad}/{pino.ciclo_de_vida} días")
    


# ==============================================================================
# ARCHIVO 59/68: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

import random
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ZanahoriaService(CultivoService):
    """Servicio para operaciones sobre el cultivo Zanahoria."""

    def __init__(self, strategy: AbsorcionAguaStrategy):
        self.strategy = strategy

    def absorver_agua(self, zanahoria: Zanahoria) -> int:
        temperatura = random.uniform(15, 30)
        humedad = random.uniform(40, 80)
        print(f"[ZanahoriaService] T={temperatura:.1f}°C, H={humedad:.1f}%")
        return self.strategy.calcular_absorcion(zanahoria, temperatura, humedad)


    def mostrar_datos(self, zanahoria: Zanahoria):
        tipo = "Baby Carrot" if zanahoria.baby_carrot else "Común"
        print(f"[ZANAHORIA] Tipo: {tipo} | Agua: {zanahoria.agua}L | "
            f"Superficie: {zanahoria.superficie} | Edad: {zanahoria.edad}/{zanahoria.ciclo_de_vida} días")



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 60/68: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 61/68: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

from typing import List, Type
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.negocio.paquete import Box


class FincasService:
    """
    Servicio de nivel superior que orquesta operaciones de plantaciones.
    """

    def __init__(self, plantacion_service: PlantacionService, registry: CultivoServiceRegistry):
        self.fincas: List[RegistroForestal] = []
        self.plantacion_service = plantacion_service
        self.registry = registry

    def add_finca(self, finca: RegistroForestal) -> None:
        """Agrega una finca (RegistroForestal) a la lista."""
        self.fincas.append(finca)

    def remover_finca(self, finca: RegistroForestal) -> None:
        """Elimina una finca existente."""
        self.fincas.remove(finca)

    def fumigar(self, id_finca: int, insecticida: str) -> None:
        """Muestra información de fumigación para cada cultivo."""
        print(f"\n[FUMIGACIÓN] Finca {id_finca} con {insecticida}")
        for finca in self.fincas:
            if finca.id_padron == id_finca:
                plantacion = finca.plantacion
                for cultivo in plantacion.cultivos:
                    servicio: CultivoService = self.registry.obtener_servicio(cultivo.__class__.__name__)
                    if servicio:
                        servicio.mostrar_datos(cultivo)

    def regar(self) -> None:
        """Riega todas las fincas registradas."""
        print("\n[RIEGO] Iniciando riego general...")
        for finca in self.fincas:
            self.plantacion_service.regar(finca.plantacion)

    def cosechar_y_empaquetar(self, tipo: Type[Cultivo]) -> Box:
        """
        Cosecha los cultivos de un tipo específico y los empaqueta en una Box<T>.
        """
        print(f"\n[COSECHA] Empaquetando cultivos de tipo {tipo.__name__}")
        box = Box[tipo]()
        for finca in self.fincas:
            for cultivo in finca.plantacion.cultivos:
                if isinstance(cultivo, tipo):
                    box.add_item(cultivo)
        box.mostrar_contenido_caja()
        return box


# ==============================================================================
# ARCHIVO 62/68: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

from typing import Generic, TypeVar, List
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar("T", bound=Cultivo)


class Box(Generic[T]):
    """Contenedor genérico para empaquetar cosechas (bounded generic)."""

    def __init__(self):
        self.items: List[T] = []

    def add_item(self, item: T) -> None:
        """Agrega un cultivo al contenedor."""
        self.items.append(item)

    def get_items(self) -> List[T]:
        """Devuelve la lista de cultivos."""
        return self.items

    def mostrar_contenido_caja(self) -> None:
        """Muestra los cultivos empaquetados."""
        print("\n=== Contenido de la caja ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print("============================\n")



################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 63/68: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 64/68: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class TrabajadorService:
    """Servicio que maneja operaciones sobre los trabajadores."""

    def asignar_apto_medico(self, trabajador, apto: bool, fecha: date, obs: str):
        """Asigna un nuevo apto médico al trabajador."""
        apto_medico = AptoMedico(apto, fecha, obs)
        trabajador.set_apto_medico(apto_medico)
        print(f"Apto médico asignado a {trabajador.get_nombre()}: {apto_medico.get_resumen()}")

    def trabajar(self, trabajador, fecha: date, herramienta):
        """Ejecuta las tareas del trabajador según su apto médico y fecha programada."""
        apto = trabajador.get_apto_medico()

        # Validar apto médico antes de trabajar
        if not apto or not apto.esta_apto():
            print(f"[ERROR] {trabajador.get_nombre()} no puede trabajar (no apto).")
            return False

        tareas = trabajador.get_tareas()
        if not tareas:
            print(f"[INFO] {trabajador.get_nombre()} no tiene tareas asignadas.")
            return False

        # Ordenar tareas por ID descendente
        tareas_ordenadas = sorted(tareas, key=lambda t: t.id, reverse=True)

        print(f"[TAREAS] Ejecutando tareas de {trabajador.get_nombre()} con {herramienta.nombre} "
              f"(Certificación: {herramienta.certificacion_seguridad})...")

        for tarea in tareas_ordenadas:
            if tarea.fecha_programada == fecha:
                tarea.completada = True
                estado = "COMPLETADA"
            else:
                estado = "PENDIENTE"

            print(f" - Tarea {tarea.id}: '{tarea.descripcion}' → {estado} "
                  f"(programada para {tarea.fecha_programada})")

        print(f"{trabajador.get_nombre()} trabajó el {fecha} con {herramienta.nombre}.\n")
        return True



################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 65/68: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 66/68: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory


class PlantacionService:
    """Servicio que gestiona operaciones de las plantaciones."""

    def __init__(self, registry: CultivoServiceRegistry):
        self.registry = registry

    def crear_plantacion(self, tierra, nombre: str, agua: int) -> Plantacion:
        plantacion = Plantacion(
            id=tierra.id,
            nombre=nombre,
            agua=agua,
            tierra=tierra,
            superficie_total=float(getattr(tierra, "superficie", 0.0))
        )
        print(f"[PLANTACIÓN] Creada '{nombre}' con {agua} L disponibles.")
        return plantacion

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> bool:
        """Agrega nuevos cultivos a la plantación (usa Factory + validaciones)."""
        muestra = CultivoFactory.crear_cultivo(especie)

        sup_por_unidad = float(getattr(muestra, "superficie", 0.0))
        cant = int(cantidad)
        sup_necesaria = sup_por_unidad * cant

        sup_disp = float(plantacion.superficie_disponible)

        if sup_disp < sup_necesaria:
            raise SuperficieInsuficienteException(
                especie, sup_necesaria, sup_disp
            )

        for _ in range(cant):
            plantacion.agregar_cultivo(CultivoFactory.crear_cultivo(especie))
            print(f" Plantado {especie} en '{plantacion.nombre}'")

        return True

    def regar(self, plantacion: Plantacion) -> bool:
        if float(plantacion.agua_disponible) < 10.0:
            raise AguaAgotadaException(plantacion.agua_disponible, 10)

        print(f"[RIEGO] Regando '{plantacion.nombre}' con {plantacion.agua_disponible} L disponibles...")
        for cultivo in plantacion.cultivos:
            servicio = self.registry.obtener_servicio(cultivo.__class__.__name__)
            if servicio:
                agua = servicio.absorver_agua(cultivo)
                cultivo.agua = float(cultivo.agua) + float(agua)
                plantacion.agua_disponible = float(plantacion.agua_disponible) - float(agua)
        return True


# ==============================================================================
# ARCHIVO 67/68: registro_forestal_services.py
# Directorio: servicios/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/registro_forestal_services.py
# ==============================================================================

import os
import pickle
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


class RegistroForestalService:
    """Servicio encargado de la persistencia del registro forestal."""

    def __init__(self, registry: CultivoServiceRegistry):
        self.registry = registry

    def persistir(self, registro: RegistroForestal) -> None:
        """Guarda un registro en disco usando pickle."""
        os.makedirs("data", exist_ok=True)
        archivo = f"data/{registro.propietario}.dat"
        try:
            with open(archivo, "wb") as f:
                pickle.dump(registro, f)
            print(f"[PERSISTENCIA] Registro '{registro.propietario}' guardado en {archivo}")
        except Exception as e:
            raise PersistenciaException("ESCRITURA", archivo, str(e))

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """Lee un registro desde disco."""
        archivo = f"data/{propietario}.dat"
        try:
            with open(archivo, "rb") as f:
                registro = pickle.load(f)
            print(f"[LECTURA] Registro '{propietario}' leído correctamente.")
            return registro
        except FileNotFoundError:
            raise PersistenciaException("LECTURA", archivo, "Archivo no encontrado.")
        except Exception as e:
            raise PersistenciaException("LECTURA", archivo, str(e))



    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """Muestra información completa del registro forestal."""
        print("\n" + "=" * 70)
        print("REGISTRO FORESTAL")
        print("=" * 70)
        print(f"Propietario: {registro.propietario}")
        print(f"Avalúo fiscal: ${registro.avaluo:,.2f}")
        print(f"ID Padrón: {registro.id_padron}\n")
    
        print("--- TERRENO ---")
        print(f"Ubicación: {registro.tierra.domicilio}")
        print(f"Superficie: {registro.tierra.superficie} m²\n")
    
        print("--- PLANTACIÓN ---")
        print(f"Nombre: {registro.plantacion.nombre}")
        print(f"Agua disponible: {registro.plantacion.agua_disponible} L")
        print(f"Cultivos: {len(registro.plantacion.cultivos)}")
        print(f"Trabajadores: {len(registro.plantacion.trabajadores)}")
        print("=" * 70 + "\n")



# ==============================================================================
# ARCHIVO 68/68: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """Servicio para creación y gestión de tierras."""

    def crear_tierra(self, id: int, superficie: float, domicilio: str) -> Tierra:
        """Crea un terreno sin plantación asociada."""
        tierra = Tierra(id=id, superficie=superficie, domicilio=domicilio)
        print(f"[TIERRA] Creada tierra {tierra.id} en {tierra.domicilio} ({tierra.superficie} m²)")
        return tierra

    def crear_tierra_con_plantacion(self, id: int, superficie: float, domicilio: str, nombre_plantacion: str) -> Tierra:
        """Crea una tierra y su plantación asociada."""
        tierra = Tierra(id=id, superficie=superficie, domicilio=domicilio)
        plantacion = Plantacion(id=id, nombre=nombre_plantacion, agua=superficie / 10, tierra=tierra)
        tierra.set_finca(plantacion)
        print(f"[TIERRA] Creada tierra + plantación '{nombre_plantacion}' en {domicilio}")
        return tierra



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 67
# Generado: 2025-10-22 09:45:41
################################################################################
