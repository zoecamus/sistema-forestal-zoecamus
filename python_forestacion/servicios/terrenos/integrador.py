"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: registro_forestal_services.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/registro_forestal_services.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

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


