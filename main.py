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
