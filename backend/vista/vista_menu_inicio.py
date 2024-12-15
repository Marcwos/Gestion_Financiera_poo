
from vista.vistamenu_categorias import menu_categoria  
from vista.vistamenu_metas import menu_metas  
from vista.vistamenu_informes import menu_informes  
from controllers.factory import TransaccionFactory
lista_categorias = []


def mostrar_menu_inicio():
    print("\n=== MENÚ DE CUENTAS ===")
    print("1. Ingresar gastos")
    print("2. Ingresar ingresos")
    print("3. Cuenta")
    print("4. Categorías")
    print("5. Gestionar Metas")
    print("6. Generar Informe")
    print("7. Logout")
    print("========================")

def menu_cuenta(usuario, lista_transacciones):
    while True:
        mostrar_menu_inicio()  # Llama a la función del menú
        opcion_menu = input("Seleccione una opción: ")

        if opcion_menu == '1':
            ingresar_gastos(usuario, lista_transacciones)  # Manejar ingreso de gastos
        elif opcion_menu == '2':
            ingresar_ingresos(usuario, lista_transacciones)  # Manejar ingreso de ingresos
        elif opcion_menu == '3':
            menu_cuenta(usuario, lista_transacciones)  # Manejar la cuenta (ya definido)
        elif opcion_menu == '4':
            menu_categoria(usuario)  # Llama al menú de categorías
        elif opcion_menu == '5':
            menu_metas(usuario)  # Llama al menú de metas
        elif opcion_menu == '6':
            menu_informes(lista_transacciones)  # Llama al menú de informes
        elif opcion_menu == '7':
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def ingresar_transaccion(usuario, lista_transacciones, tipo_transaccion):
    descripcion = input(f"Ingrese la descripción del {tipo_transaccion.lower()}: ")
    monto = float(input(f"Ingrese el monto del {tipo_transaccion.lower()}: "))
    
    categoria = mostrar_categorias(usuario)
    if categoria is None:
        print("Categoría no válida. Transacción no registrada.")
        return
    
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    id_cuenta = input("Ingrese el ID de la cuenta: ")

    cuenta_encontrada = next((cuenta for cuenta in usuario.get_cuentas() if cuenta.get_id_cuenta() == id_cuenta), None)

    if cuenta_encontrada:
        transaccion = TransaccionFactory.crear_transaccion(tipo_transaccion, monto, categoria.nombre_categoria, fecha, descripcion)
        
        cuenta_encontrada.agregar_transaccion(transaccion)
        lista_transacciones.append(transaccion)

        print(f"{tipo_transaccion} registrado exitosamente.")
    else:
        print("La cuenta no existe.")

# Funciones específicas
def ingresar_gastos(usuario, lista_transacciones):
    ingresar_transaccion(usuario, lista_transacciones, "Gasto")

def ingresar_ingresos(usuario, lista_transacciones):
    ingresar_transaccion(usuario, lista_transacciones, "Ingreso")


def mostrar_categorias(usuario):
    print("Categorías disponibles:")
    for idx, categoria in enumerate(usuario.lista_categorias):
        print(f"{idx + 1}. {categoria.nombre_categoria} - {categoria.descripcion} ({categoria.tipo})")

    seleccion = int(input("Seleccione el número de la categoría: ")) - 1
    if 0 <= seleccion < len(usuario.lista_categorias):
        return usuario.lista_categorias[seleccion]
    else:
        print("Selección inválida.")
        return None