from controllers.user_controller import Usuario 
from controllers.factory import TransaccionFactory
from controllers.inform_controller import Informe,EstrategiaInformeGastos, EstrategiaInformeIngresos, EstrategiaInformeNeto
from controllers.goals_finance_controller import MetaFinanciera
from datetime import date, datetime

def menu_metas_opciones():
    print("\n=== GESTIÓN DE METAS ===")
    print("1. Agregar meta")
    print("2. Eliminar meta")
    print("3. Mostrar metas")
    print("4. Salir")

def seleccionar_opcion_metas():
    return input("Seleccione una opción: ")

def menu_metas(usuario):
    while True:
        menu_metas_opciones()
        opcion = seleccionar_opcion_metas()

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la meta: ")
            monto = float(input("Ingrese el monto de la meta: "))
            fecha_limite = input("Ingrese la fecha límite (YYYY-MM-DD): ")
            meta = MetaFinanciera(descripcion, monto, fecha_limite)  # Implementa o importa esta clase desde controllers
            usuario.agregar_meta(meta)  # Implementa o importa este método desde controllers
            print("Meta agregada exitosamente.")
        elif opcion == '2':
            descripcion = input("Ingrese la descripción de la meta a eliminar: ")
            usuario.eliminar_meta(descripcion)
        elif opcion == '3':
            usuario.mostrar_metas()
        elif opcion == '4':
            print("Saliendo del menú de metas...")
            break
        else:
            print("Opción no válida.")