from controllers.account_controller import Cuenta

def menu_cuenta(usuario):
    while True:
        print("\n--- Menú de Cuentas ---")
        print("1. Agregar Cuenta")
        print("2. Eliminar Cuenta")
        print("3. Mostrar Cuentas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_cuenta = input("Ingresa el ID de la cuenta: ")
            tipo_cuenta = input("Ingresa el tipo de cuenta: ")
            nombre_cuenta = input("Ingresa el nombre de la cuenta: ")
            saldo_inicial = float(input("Ingresa el saldo inicial: "))
            # Aquí se llama al método agregar_cuenta del objeto usuario
            usuario.agregar_cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)

        elif opcion == '2':
            nombre_cuenta = input("Ingresa el nombre de la cuenta a eliminar: ")
            # Aquí se llama al método eliminar_cuenta del objeto usuario
            usuario.eliminar_cuenta(nombre_cuenta)

        elif opcion == '3':
            # Aquí se llama al método mostrar_cuentas del objeto usuario
            usuario.mostrar_cuentas()

        elif opcion == '4':
            break

        else:
            print("Opción no válida. Por favor, selecciona de nuevo.")