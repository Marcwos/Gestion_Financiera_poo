from abc import ABC, abstractmethod

# Clase base (interfaz común para categorías y subcategorías)
class ElementoCategoria(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

    @abstractmethod
    def agregar(self, elemento):
        pass

    @abstractmethod
    def eliminar(self, elemento):
        pass


# Clase hoja (categoría individual)
class Categoria(ElementoCategoria):
    def __init__(self, nombre_categoria, descripcion, tipo):
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.tipo = tipo

    def mostrar(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}- {self.nombre_categoria} ({self.tipo}): {self.descripcion}")

    def agregar(self, elemento):
        print(f"No se pueden agregar subcategorías a '{self.nombre_categoria}' porque es una categoría individual.")

    def eliminar(self, elemento):
        print(f"No se pueden eliminar subcategorías de '{self.nombre_categoria}' porque es una categoría individual.")


# Clase compuesta (categoría que puede contener subcategorías)
class CategoriaCompuesta(ElementoCategoria):
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.subcategorias = []

    def mostrar(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}+ {self.nombre_categoria}")
        for subcategoria in self.subcategorias:
            subcategoria.mostrar(nivel + 1)

    def agregar(self, elemento):
        self.subcategorias.append(elemento)
        print(f"Subcategoría '{elemento.nombre_categoria}' agregada a '{self.nombre_categoria}'.")

    def eliminar(self, elemento):
        if elemento in self.subcategorias:
            self.subcategorias.remove(elemento)
            print(f"Subcategoría '{elemento.nombre_categoria}' eliminada de '{self.nombre_categoria}'.")
        else:
            print(f"Subcategoría '{elemento.nombre_categoria}' no encontrada en '{self.nombre_categoria}'.")
