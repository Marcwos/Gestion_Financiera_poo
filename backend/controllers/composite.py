from abc import ABC, abstractmethod

# Interfaz base
class ElementoCategoria(ABC):
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def agregar(self, elemento):
        pass

    @abstractmethod
    def eliminar(self, elemento):
        pass

# Clase hoja
class Categoria(ElementoCategoria):
    def __init__(self, nombre, descripcion, tipo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo

    def mostrar(self):
        print(f"Categoría: {self.nombre} ({self.tipo}) - {self.descripcion}")

    def agregar(self, elemento):
        print("No se pueden agregar subcategorías a una categoría individual.")

    def eliminar(self, elemento):
        print("No se pueden eliminar subcategorías de una categoría individual.")

# Clase compuesta
class CategoriaCompuesta(ElementoCategoria):
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def mostrar(self):
        print(f"Categoría compuesta: {self.nombre}")
        for subcategoria in self.subcategorias:
            subcategoria.mostrar()

    def agregar(self, elemento):
        self.subcategorias.append(elemento)
        print(f"Subcategoría '{elemento.nombre}' agregada a '{self.nombre}'.")

    def eliminar(self, elemento):
        self.subcategorias.remove(elemento)
        print(f"Subcategoría '{elemento.nombre}' eliminada de '{self.nombre}'.")
