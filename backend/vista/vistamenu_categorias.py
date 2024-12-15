from controllers.user_controller import Usuario 
from controllers.factory import TransaccionFactory
from controllers.inform_controller import Informe,EstrategiaInformeGastos, EstrategiaInformeIngresos, EstrategiaInformeNeto
from controllers.goals_finance_controller import MetaFinanciera
from datetime import date, datetime

def mostrar_menu_categorias():
    print("\nMenú de Categorías")
    print("1. Agregar categoría")
    print("2. Eliminar categoría")
    print("3. Modificar categoría")
    print("4. Mostrar categorías")
    print("5. Salir")

def seleccionar_opcion_categorias():
    return input("Seleccione una opción: ")

def menu_categoria(usuario):
    while True:
        mostrar_menu_categorias()
        opcion = seleccionar_opcion_categorias()

        if opcion == '1':
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
            descripcion = input("Ingrese una descripción para la categoría: ")
            tipo = input("Ingrese el tipo de la categoría (Ingreso o Gasto): ")
            usuario.agregar_categoria(nombre_categoria, descripcion, tipo)
        elif opcion == '2':
            nombre_categoria = input("Ingrese el nombre de la categoría a eliminar: ")
            usuario.eliminar_categoria(nombre_categoria)
        elif opcion == '3':
            modificar_categoria(usuario)  # Implementa o importa este método desde controllers
        elif opcion == '4':
            usuario.mostrar_categorias()
        elif opcion == '5':
            print("Saliendo del menú de categorías...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")