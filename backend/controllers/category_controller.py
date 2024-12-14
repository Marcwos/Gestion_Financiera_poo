from abc import ABC, abstractmethod

# Clase base (interfaz común para categorías y subcategorías)
class ElementoCategoria(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        """Muestra la categoría o subcategoría en el nivel indicado."""
        pass

    @abstractmethod
    def agregar(self, elemento):
        """Agrega un elemento (categoría o subcategoría)."""
        pass

    @abstractmethod
    def eliminar(self, elemento):
        """Elimina un elemento (categoría o subcategoría)."""
        pass


# Clase hoja (categoría individual)
class Categoria(ElementoCategoria):
    def __init__(self, nombre_categoria, descripcion, tipo):
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.tipo = tipo

    def mostrar(self, nivel=0):
        """Muestra la categoría individual."""
        indentacion = "  " * nivel
        print(f"{indentacion}- {self.nombre_categoria} ({self.tipo}): {self.descripcion}")

    def agregar(self, elemento):
        # LSP (Principio de Sustitución de Liskov)
        raise NotImplementedError("No se pueden agregar subcategorías a una categoría individual.")

    def eliminar(self, elemento):
        # LSP (Principio de Sustitución de Liskov)
        raise NotImplementedError("No se pueden eliminar subcategorías de una categoría individual.")


# Clase compuesta (categoría compuesta que puede contener subcategorías)
class CategoriaCompuesta(ElementoCategoria):
    def __init__(self, nombre_categoria, descripcion):
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.elementos = []  # Lista para almacenar subcategorías

    def mostrar(self, nivel=0):
        """Muestra la categoría compuesta y sus subcategorías."""
        indentacion = "  " * nivel
        print(f"{indentacion}- {self.nombre_categoria} (Compuesta): {self.descripcion}")
        for elemento in self.elementos:
            elemento.mostrar(nivel + 1)  # Llamada recursiva para mostrar subcategorías

    def agregar(self, elemento):
        """Agrega una subcategoría a la categoría compuesta."""
        self.elementos.append(elemento)  # SRP (Principio de Responsabilidad Única)
        
    def eliminar(self, elemento):
        """Elimina una subcategoría de la categoría compuesta."""
        self.elementos.remove(elemento)  # SRP (Principio de Responsabilidad Única)