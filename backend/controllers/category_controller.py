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

# Modificar categoría
def modificar_categoria(usuario):
    nombre_categoria = input("Ingrese el nombre de la categoría a modificar: ")
    nombre_categorianuevo = input("Ingrese el nuevo nombre de la categoría: ")
    descripcion = input("Ingrese nueva descripción para la categoría: ")
    tipo = input("Ingrese tipo de la categoría a modificar (Ingreso o Gasto): ")
    usuario.modificar_categoria(nombre_categoria, nombre_categorianuevo, descripcion, tipo)
