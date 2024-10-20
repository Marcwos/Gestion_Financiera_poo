from controllers.user_controller import Usuario 
from controllers.transaction_controller import Transaccion
from controllers.account_controller import Cuenta
from controllers.transaction_controller import TransaccionIngreso, TransaccionGasto
from controllers.category_controller import Categoria  
from controllers.inform_controller import Informe
from controllers.goals_finance_controller import MetaFinanciera
from datetime import date

lista_categorias = []
lista_transacciones = []

print("-----Bienvenido a la aplicación Money Wise-----")

def mostrar_menu():
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def mostrar_crear_cuenta():
    print("\nMenú de Cuentas:")
    print("1. Agregar cuenta")
    print("2. Eliminar cuenta")
    print("3. Mostrar cuentas")
    print("4. Salir")

def mostrar_menu_categorias():
    print("\n menu de categorias")
    print("1. Agregar categoría")
    print("2. Eliminar categoría")
    print("3. Modificar categoría")
    print("4. Mostrar categorías")
    print("5. Salir")

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(nombre, email, password)
    Usuario.usuarios_registrados.append(nuevo_usuario)
    print(f"Usuario {nombre} registrado exitosamente.")

def iniciar_sesion():
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")

    for usuario in Usuario.usuarios_registrados:
        if usuario.email == email and usuario.get_password() == password:
            print(f"Bienvenido, {usuario.nombre}!")
            return usuario

    print("Credenciales incorrectas. Intente nuevamente.")
    return None  # Asegúrate de retornar None si las credenciales son incorrectas

def agregar_cuenta(usuario):
    id_cuenta = input("Ingrese el ID de la cuenta: ")
    tipo_cuenta = input("Ingrese el tipo de cuenta: ")
    nombre_cuenta = input("Ingrese el nombre de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    
    # Llama al método agregar_cuenta de la clase Usuario
    usuario.agregar_cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)

def eliminar_cuenta(usuario):
    nombre_cuenta = input("Ingrese el nombre de la cuenta a eliminar: ")
    usuario.eliminar_cuenta(nombre_cuenta)

def mostrar_cuentas(usuario):
    usuario.mostrar_cuentas()

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

def ingresar_gastos(usuario, lista_transacciones):
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    
    # Mostrar categorías y permitir selección
    categoria = mostrar_categorias(usuario)
    if categoria is None:
        print("Categoría no válida. Gasto no registrado.")
        return
    
    fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
    id_cuenta = input("Ingrese el ID de la cuenta: ")

    # Buscar la cuenta por ID
    cuenta_encontrada = None
    for cuenta in usuario.get_cuentas():
        if cuenta.get_id_cuenta() == id_cuenta:
            cuenta_encontrada = cuenta
            break

    if cuenta_encontrada:
        # Crear transacción de gasto
        transaccion = TransaccionGasto(monto, categoria.nombre_categoria, fecha, descripcion)
        cuenta_encontrada.agregar_transaccion(transaccion)

        # Agregar la transacción a la lista de transacciones del usuario
        usuario.lista_transacciones.append(transaccion)

        print("Gasto registrado exitosamente.")
    else:
        print("La cuenta no existe.")

def ingresar_ingresos(usuario, lista_transacciones):
    descripcion = input("Ingrese la descripción del ingreso: ")
    monto = float(input("Ingrese el monto del ingreso: "))
    
    # Mostrar categorías y permitir selección
    categoria = mostrar_categorias(usuario)
    if categoria is None:
        print("Categoría no válida. Ingreso no registrado.")
        return
    
    fecha = input("Ingrese la fecha del ingreso (YYYY-MM-DD): ")
    id_cuenta = input("Ingrese el ID de la cuenta: ")

    # Buscar la cuenta por ID
    cuenta_encontrada = None
    for cuenta in usuario.get_cuentas():
        if cuenta.get_id_cuenta() == id_cuenta:
            cuenta_encontrada = cuenta
            break

    if cuenta_encontrada:
        # Crear la transacción de ingreso
        transaccion = TransaccionIngreso(monto, categoria.nombre_categoria, fecha, descripcion)
        cuenta_encontrada.agregar_transaccion(transaccion)

        # Agregar la transacción a la lista de transacciones del usuario
        usuario.lista_transacciones.append(transaccion)

        print("Ingreso registrado exitosamente.")
    else:
        print("La cuenta no existe.")

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

def menu_categoria(usuario):
    while True:
        mostrar_menu_categorias()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
            descripcion = input("Ingrese una descripción para la categoría: ")
            tipo = input("Ingrese el tipo de la categoría (Ingreso o Gasto): ")
            usuario.agregar_categoria(nombre_categoria, descripcion, tipo)
        elif opcion == '2':
            nombre_categoria = input("Ingrese el nombre de la categoría a eliminar: ")
            usuario.eliminar_categoria(nombre_categoria)
        elif opcion == '3':
            nombre_categoria = input("Ingrese el nombre de la categoría a modificar: ")
            nombre_categorianuevo = input("Ingrese el nombre de la categoría a modificar: ")
            descripcion = input("Ingrese nueva descripción para la categoría: ")
            tipo = input("Ingrese  tipo de la categoría a modificar (Ingreso o Gasto): ")
            usuario.modificar_categoria(nombre_categoria,nombre_categorianuevo, descripcion, tipo)
        elif opcion == '4':
            usuario.mostrar_categorias()
        elif opcion == '5':
            print("Saliendo del menú de categorías...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_informes(lista_transacciones):
    print("\n=== GENERAR INFORMES ===")
    print("1. Informe de ingresos")
    print("2. Informe de gastos")
    print("3. Informe neto")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")

    if opcion in ['1', '2', '3']:
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

        # Crear instancia del informe
        tipo_informe = ""
        if opcion == '1':
            tipo_informe = "ingreso"
        elif opcion == '2':
            tipo_informe = "gastos"
        elif opcion == '3':
            tipo_informe = "neto"

        informe = Informe(tipo_informe)
        resultado = informe.generar_informe(lista_transacciones, fecha_inicio, fecha_fin)
        
       
        print(resultado)
    elif opcion == '4':
        return  
    else:
        print("Opción no válida.")

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
            menu_informes(usuario.lista_transacciones)  
        elif opcion_menu == '7':
            print("Cerrando sesión...")
            break
        else:
            print("Opción invalida. Intente nuevamente.")

def menu_metas(usuario): 
    while True:
        print("\n=== GESTIÓN DE METAS ===")
        print("1. Registrar nueva meta")
        print("2. Verificar cumplimiento de metas")
        print("3. Volver al menú principal")
        print("========================")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_meta = input("Ingrese el ID de la meta: ")
            descripcion = input("Ingrese la descripción de la meta: ")
            valor_objetivo = float(input("Ingrese el valor objetivo: "))

            try:
                fecha_limite = date.fromisoformat(input("Ingrese la fecha límite (YYYY-MM-DD): "))
            except ValueError:
                print("Fecha inválida. Intente nuevamente.")
                continue

            nueva_meta = MetaFinanciera(id_meta, valor_objetivo, fecha_limite, descripcion)
            nueva_meta.registrar_meta(usuario.lista_metas) 
            print("Meta registrada exitosamente.")

        elif opcion == '2':
            if not usuario.lista_metas:
                print("No hay metas registradas.")
            else:
                id_cuenta = input("Ingrese el ID de la cuenta para verificar las metas: ")
                cuenta = None
                for c in usuario.get_cuentas():
                    if c.get_id_cuenta() == id_cuenta:  
                        cuenta = c
                        break

                if cuenta is None:
                    print("Cuenta no encontrada.")
                else:
                    for meta in usuario.lista_metas:
                        print(f"\nMeta: {meta.get_descripcion()}")  
                        meta.verificar_cumplimiento(cuenta)

        elif opcion == '3':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

            
def main():
    lista_metas = []  
    lista_transacciones = [] 

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:
                menu_cuentaPRI(usuario, lista_metas, lista_transacciones)
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()  