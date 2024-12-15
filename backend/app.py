from views.menu_views import mostrar_menu
from controllers.user_controller import registrar_usuario, iniciar_sesion
from views.account_views import menu_cuentaPRI


lista_categorias = []

print("-----Bienvenido a la aplicación Money Wise-----")

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