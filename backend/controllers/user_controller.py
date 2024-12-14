from controllers.account_controller import Cuenta 
from controllers.category_controller import Categoria, CategoriaCompuesta

class Usuario:
    usuarios_registrados = []

    def __init__(self, nombre, email, password, saldo_actual=0, historial_transacciones=None):
        self.nombre = nombre
        self.email = email
        self.__password = password 
        self.__saldo_actual = saldo_actual 
        self.__historial_transacciones = historial_transacciones if historial_transacciones is not None else [] 
        self.__cuentas = [] 
        self.lista_categorias = []
        self.lista_metas = []        
        self.lista_transacciones = [] 

    # SRP
    def get_password(self):
        return self.__password

    # SRP
    def set_password(self, new_password):
        self.__password = new_password

    # SRP
    def get_saldo_actual(self):
        return self.__saldo_actual

    # SRP
    def set_saldo_actual(self, new_saldo):
        self.__saldo_actual = new_saldo

    # SRP
    def get_historial_transacciones(self):
        return self.__historial_transacciones

    # SRP
    def set_historial_transacciones(self, nuevo_historial):
        self.__historial_transacciones = nuevo_historial

    # SRP
    def get_cuentas(self):
        return self.__cuentas

    # SRP
    def agregar_cuenta(self, id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial=0):
        nueva_cuenta = Cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)
        self.__cuentas.append(nueva_cuenta)
        print(f"Cuenta {nombre_cuenta} de tipo {tipo_cuenta} agregada exitosamente.")

    # SRP
    def eliminar_cuenta(self, nombre_cuenta):
        for cuenta in self.get_cuentas():
            if cuenta.get_nombre_cuenta() == nombre_cuenta:
                self.__cuentas.remove(cuenta)
                print(f"Cuenta {nombre_cuenta} eliminada exitosamente.")
                return
        print(f"No se encontró la cuenta {nombre_cuenta}.")

    # SRP
    def mostrar_cuentas(self):
        if not self.get_cuentas():
            print(f"El usuario {self.nombre} no tiene cuentas.")
        else:
            print(f"Cuentas del usuario {self.nombre}:")
            for cuenta in self.get_cuentas():
                print(f"- {cuenta.get_nombre_cuenta()} (Tipo: {cuenta.get_tipo_cuenta()}, Saldo: {cuenta.get_saldo()})")

    # SRP
    def agregar_categoria(self, nombre_categoria, descripcion, tipo, categoria_padre=None):
        """Agrega una nueva categoría o subcategoría."""
        nueva_categoria = Categoria(nombre_categoria, descripcion, tipo)

        if categoria_padre is None:
            self.lista_categorias.append(nueva_categoria)
            print(f"Categoría '{nombre_categoria}' agregada al nivel raíz.")
        else:
            for categoria in self.lista_categorias:
                if isinstance(categoria, CategoriaCompuesta) and categoria.nombre_categoria == categoria_padre:
                    categoria.agregar(nueva_categoria)
                    print(f"Categoría '{nombre_categoria}' agregada como subcategoría de '{categoria_padre}'.")
                    return
            print(f"No se encontró la categoría compuesta '{categoria_padre}'.")

    # SRP
    def eliminar_categoria(self, nombre_categoria):
        """Elimina una categoría o subcategoría por su nombre."""
        for categoria in self.lista_categorias:
            if categoria.nombre_categoria == nombre_categoria:
                self.lista_categorias.remove(categoria)
                print(f"Categoría '{nombre_categoria}' eliminada del nivel raíz.")
                return
            elif isinstance(categoria, CategoriaCompuesta):
                categoria.eliminar(Categoria(nombre_categoria, "", ""))
                return
        print(f"No se encontró la categoría '{nombre_categoria}' en el nivel raíz.")

    # SRP
    def mostrar_categorias(self):
        """Muestra todas las categorías, incluyendo jerarquías."""
        if not self.lista_categorias:
            print("No hay categorías registradas.")
        else:
            print("Categorías registradas:")
            for categoria in self.lista_categorias:
                categoria.mostrar()

    # SRP
    def modificar_categoria(self, nombre_actual, nuevo_nombre, nueva_descripcion, nuevo_tipo):
        """Modifica una categoría existente por su nombre."""
        for categoria in self.lista_categorias:
            if categoria.nombre_categoria == nombre_actual:
                categoria.modificar_categoria(nuevo_nombre, nueva_descripcion, nuevo_tipo)
                return
            elif isinstance(categoria, CategoriaCompuesta):
                self._modificar_categoria_recursiva(categoria, nombre_actual, nuevo_nombre, nueva_descripcion, nuevo_tipo)
                return
        print(f"No se encontró la categoría '{nombre_actual}'.")

    # SRP
    def _modificar_categoria_recursiva(self, categoria_compuesta, nombre_actual, nuevo_nombre, nueva_descripcion, nuevo_tipo):
        """Busca y modifica una categoría dentro de una estructura jerárquica."""
        for subcategoria in categoria_compuesta.subcategorias:
            if subcategoria.nombre_categoria == nombre_actual:
                subcategoria.modificar_categoria(nuevo_nombre, nueva_descripcion, nuevo_tipo)
                print(f"Categoría '{nombre_actual}' modificada exitosamente.")
                return
            elif isinstance(subcategoria, CategoriaCompuesta):
                self._modificar_categoria_recursiva(subcategoria, nombre_actual, nuevo_nombre, nueva_descripcion, nuevo_tipo)
