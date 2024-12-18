from abc import ABC, abstractmethod

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

class Categoria(ElementoCategoria):
    def __init__(self, nombre_categoria, descripcion, tipo):
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.tipo = tipo

    def mostrar(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}- {self.nombre_categoria} ({self.tipo}): {self.descripcion}")

    # SRP
    def agregar(self, elemento):
        raise NotImplementedError("No se pueden agregar subcategorías a una categoría individual.")

    # SRP
    def eliminar(self, elemento):
        raise NotImplementedError("No se pueden eliminar subcategorías de una categoría individual.")


class CategoriaCompuesta(ElementoCategoria):
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.subcategorias = []

    def mostrar(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}+ {self.nombre_categoria}")
        for subcategoria in self.subcategorias:
            subcategoria.mostrar(nivel + 1)

    def agregar(self, elemento: ElementoCategoria):
        self.subcategorias.append(elemento)
        print(f"Subcategoría '{elemento.nombre_categoria}' agregada a '{self.nombre_categoria}'.")

    def eliminar(self, elemento: ElementoCategoria):
        if elemento in self.subcategorias:
            self.subcategorias.remove(elemento)
            print(f"Subcategoría '{elemento.nombre_categoria}' eliminada de '{self.nombre_categoria}'.")
        else:
           print(f"Subcategoría '{elemento.nombre}' eliminada de '{self.nombre}'.")