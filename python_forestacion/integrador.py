"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/constantes.py
# ================================================================================

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



