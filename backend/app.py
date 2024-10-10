from controllers.user_controller import Usuario 

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

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()

        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:
                menu_cuenta(usuario)  # Maneja el menú de cuentas aquí

        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
