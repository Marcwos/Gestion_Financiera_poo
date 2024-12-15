from views.menu_views import mostrar_menu_categorias
from controllers.category_controller import modificar_categoria

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