from models.inform_model import Informe
from controllers.inform_controller import obtener_fechas, crear_estrategia

def menu_informes(lista_transacciones):
    print("\n=== GENERAR INFORMES ===")
    print("1. Informe de ingresos")
    print("2. Informe de gastos")
    print("3. Informe neto")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")

    if opcion in ['1', '2', '3']:
        fecha_inicio, fecha_fin = obtener_fechas()  # Se extrae a función para seguir SRP

        estrategia = crear_estrategia(opcion)  # Se extrae a función para mejorar la claridad

        informe = Informe(estrategia)
        resultado = informe.generar_informe(lista_transacciones, fecha_inicio, fecha_fin)
        print(resultado)

    elif opcion == '4':
        return
    else:
        print("Opción no válida.")