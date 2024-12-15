from controllers.user_controller import Usuario 
from controllers.factory import TransaccionFactory
from controllers.inform_controller import Informe,EstrategiaInformeGastos, EstrategiaInformeIngresos, EstrategiaInformeNeto
from controllers.goals_finance_controller import MetaFinanciera
from datetime import date, datetime

def menu_informes_opciones():
    print("\n=== GENERAR INFORMES ===")
    print("1. Informe de ingresos")
    print("2. Informe de gastos")
    print("3. Informe neto")
    print("4. Volver al menú principal")

def seleccionar_opcion_informes():
    return input("Seleccione una opción: ")

def menu_informes(lista_transacciones):
    while True:
        menu_informes_opciones()
        opcion = seleccionar_opcion_informes()

        if opcion in ['1', '2', '3']:
            fecha_inicio, fecha_fin = obtener_fechas()  # Implementa o importa este método desde controllers
            estrategia = crear_estrategia(opcion)  # Implementa o importa este método desde controllers
            informe = Informe(estrategia)  # Implementa o importa este método desde controllers
            resultado = informe.generar_informe(lista_transacciones, fecha_inicio, fecha_fin)
            print(resultado)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")