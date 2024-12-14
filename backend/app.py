from controllers.user_controller import Usuario 
from controllers.factory import TransaccionFactory
from controllers.inform_controller import Informe, EstrategiaInformeGastos, EstrategiaInformeIngresos, EstrategiaInformeNeto
from controllers.goals_finance_controller import MetaFinanciera
from datetime import date, datetime

lista_categorias = []

print("-----Bienvenido a la aplicación Money Wise-----")

# Menú de la aplicación
def mostrar_menu():
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

# Menú de cuentas
def mostrar_crear_cuenta():
    print("\nMenú de Cuentas:")
    print("1. Agregar cuenta")
    print("2. Eliminar cuenta")
    print("3. Mostrar cuentas")
    print("4. Salir")

# Menú de categorías
def mostrar_menu_categorias():
    print("\nMenu de Categorías")
    print("1. Agregar categoría")
    print("2. Eliminar categoría")
    print("3. Modificar categoría")
    print("4. Mostrar categorías")
    print("5. Salir")

# Registro de usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(nombre, email, password)
    Usuario.usuarios_registrados.append(nuevo_usuario)
    print(f"Usuario {nombre} registrado exitosamente.")

# Inicio de sesión
def iniciar_sesion():
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")

    for usuario in Usuario.usuarios_registrados:
        if usuario.email == email and usuario.get_password() == password:
            print(f"Bienvenido, {usuario.nombre}!")
            return usuario

    print("Credenciales incorrectas. Intente nuevamente.")
    return None  

# Agregar cuenta
def agregar_cuenta(usuario):
    id_cuenta = input("Ingrese el ID de la cuenta: ")
    tipo_cuenta = input("Ingrese el tipo de cuenta: ")
    nombre_cuenta = input("Ingrese el nombre de la cuenta: ")
    saldo_inicial = obtener_saldo_inicial()  # Extraído a función para seguir SRP (Single Responsibility Principle)
    
    usuario.agregar_cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)

# Obtener saldo inicial
def obtener_saldo_inicial():
    return float(input("Ingrese el saldo inicial: "))  # Se encapsula la entrada de saldo para mantener la responsabilidad única

# Eliminar cuenta
def eliminar_cuenta(usuario):
    nombre_cuenta = input("Ingrese el nombre de la cuenta a eliminar: ")
    usuario.eliminar_cuenta(nombre_cuenta)

# Mostrar cuentas
def mostrar_cuentas(usuario):
    usuario.mostrar_cuentas()

# Menú de cuentas
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

# Ingresar transacción
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

# Mostrar categorías
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

# Menú de categorías
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
            modificar_categoria(usuario)  # Se extrae a una función para mejorar la claridad
        elif opcion == '4':
            usuario.mostrar_categorias()
        elif opcion == '5':
            print("Saliendo del menú de categorías...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Modificar categoría
def modificar_categoria(usuario):
    nombre_categoria = input("Ingrese el nombre de la categoría a modificar: ")
    nombre_categorianuevo = input("Ingrese el nuevo nombre de la categoría: ")
    descripcion = input("Ingrese nueva descripción para la categoría: ")
    tipo = input("Ingrese tipo de la categoría a modificar (Ingreso o Gasto): ")
    usuario.modificar_categoria(nombre_categoria, nombre_categorianuevo, descripcion, tipo)

# Menú de informes
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

# Obtener fechas
def obtener_fechas():
    fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (YYYY-MM-DD): "), "%Y-%m-%d").date()
    fecha_fin = datetime.strptime(input("Ingrese la fecha de fin (YYYY-MM-DD): "), "%Y-%m-%d").date()
    return fecha_inicio, fecha_fin

# Crear estrategia
def crear_estrategia(opcion):
    if opcion == '1':
        return EstrategiaInformeIngresos()
    elif opcion == '2':
        return EstrategiaInformeGastos()
    elif opcion == '3':
        return EstrategiaInformeNeto()

# Menú principal de cuentas
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

# Menú de metas
def menu_metas(usuario): 
    while True:
        print("\n=== GESTIÓN DE METAS ===")
        print("1. Agregar meta")
        print("2. Eliminar meta")
        print("3. Mostrar metas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la meta: ")
            monto = float(input("Ingrese el monto de la meta: "))
            fecha_limite = input("Ingrese la fecha límite (YYYY-MM-DD): ")
            meta = MetaFinanciera(descripcion, monto, fecha_limite)
            usuario.agregar_meta(meta)
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

# Bucle principal
if __name__ == '__main__':
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:  # Si se inicia sesión con éxito
                menu_cuentaPRI(usuario, usuario.lista_metas, usuario.lista_transacciones)
        elif opcion == '3':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()  