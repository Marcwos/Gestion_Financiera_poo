class Categoria:
    def __init__(self, nombre_categoria, descripcion, tipo):
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.tipo = tipo

    def agregar_categoria(self, lista_categorias):
        lista_categorias.append(self)
        print(f"Categoría '{self.nombre_categoria}' agregada exitosamente.")

    def eliminar_categoria(self, lista_categorias):
        for categoria in lista_categorias:
            if categoria.nombre_categoria == self.nombre_categoria:
                lista_categorias.remove(categoria)
                print(f"Categoría '{self.nombre_categoria}' eliminada exitosamente.")
                return
        print(f"Categoría '{self.nombre_categoria}' no encontrada.")

    def modificar_categoria(self, nuevo_nombre, nueva_descripcion, nuevo_tipo):
        self.nombre_categoria = nuevo_nombre
        self.descripcion = nueva_descripcion
        self.tipo = nuevo_tipo
        print(f"Categoría modificada a: {self.nombre_categoria}, {self.descripcion}, {self.tipo}.")
