from vista.vista_menu_inicio import menu_cuenta
from controllers.user_controller import Usuario

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

def menu_principal():
    while True:
        # Lógica de menú de inicio
        print("-----Bienvenido a la aplicación Money Wise-----")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:
                lista_transacciones = []  # Define esta lista según tu lógica
                menu_cuenta(usuario, lista_transacciones)  # Llama al menú de cuentas
        elif opcion == '3':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    menu_principal()