from views.menu_views import mostrar_crear_cuenta
from controllers.account_controller import eliminar_cuenta, mostrar_cuentas
from views.category_views import menu_categoria
from controllers.transaction_controller import ingresar_gastos, ingresar_ingresos
from views.inform_views import menu_informes
from views.goals_views import menu_metas

def menu_cuenta(usuario):
    while True:
        mostrar_crear_cuenta()
        opcion_menu = input("Seleccione una opción: ")

        if opcion_menu == '1':
            agregar_cuenta(usuario)
        elif opcion_menu == '2':
            eliminar_cuenta(usuario)
        elif opcion_menu == '3':
            mostrar_cuentas(usuario)
        elif opcion_menu == '4':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_cuentaPRI(usuario, lista_metas, lista_transacciones):
    while True:
        print("\n=== MENÚ DE CUENTAS ===")
        print("1. Ingresar gastos")
        print("2. Ingresar ingresos")
        print("3. Cuenta")
        print("4. Categorías")
        print("5. Gestionar Metas")
        print("6. Generar Informe")
        print("7. Logout")
        print("========================")

        opcion_menu = input("Seleccione una opción: ")

        if opcion_menu == '1':
            ingresar_gastos(usuario, lista_transacciones)
        elif opcion_menu == '2':
            ingresar_ingresos(usuario, lista_transacciones)
        elif opcion_menu == '3':
            menu_cuenta(usuario)
        elif opcion_menu == '4':
            menu_categoria(usuario)
        elif opcion_menu == '5':
            menu_metas(usuario)
        elif opcion_menu == '6':
            menu_informes(lista_transacciones)  
        elif opcion_menu == '7':
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def agregar_cuenta(usuario):
    id_cuenta = input("Ingrese el ID de la cuenta: ")
    tipo_cuenta = input("Ingrese el tipo de cuenta: ")
    nombre_cuenta = input("Ingrese el nombre de la cuenta: ")
    saldo_inicial = obtener_saldo_inicial()
    
    usuario.agregar_cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)

# Obtener saldo inicial
def obtener_saldo_inicial():
    return float(input("Ingrese el saldo inicial: "))  