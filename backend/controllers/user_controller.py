from controllers.account_controller import Cuenta 
from controllers.category_controller import Categoria

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

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_saldo_actual(self):
        return self.__saldo_actual

    def set_saldo_actual(self, new_saldo):
        self.__saldo_actual = new_saldo

    def get_historial_transacciones(self):
        return self.__historial_transacciones

    def set_historial_transacciones(self, nuevo_historial):
        self.__historial_transacciones = nuevo_historial

    def get_cuentas(self):
        return self.__cuentas

    def agregar_cuenta(self, id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial=0):
        nueva_cuenta = Cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)
        self.__cuentas.append(nueva_cuenta)
        print(f"Cuenta {nombre_cuenta} de tipo {tipo_cuenta} agregada exitosamente.")

    def eliminar_cuenta(self, nombre_cuenta):
        for cuenta in self.get_cuentas():  # Cambiado de self.cuentas a self.get_cuentas()
            if cuenta.get_nombre_cuenta() == nombre_cuenta:  # Cambiado a get_nombre_cuenta()
                self.__cuentas.remove(cuenta)
                print(f"Cuenta {nombre_cuenta} eliminada exitosamente.")
                return
        print(f"No se encontró la cuenta {nombre_cuenta}.")

    def mostrar_cuentas(self):
        if not self.get_cuentas():  # Cambiado de self.cuentas a self.get_cuentas()
            print(f"El usuario {self.nombre} no tiene cuentas.")
        else:
            print(f"Cuentas del usuario {self.nombre}:")
            for cuenta in self.get_cuentas():  # Cambiado de self.cuentas a self.get_cuentas()
                print(f"- {cuenta.get_nombre_cuenta()} (Tipo: {cuenta.get_tipo_cuenta()}, Saldo: {cuenta.get_saldo()})")

    def agregar_categoria(self, nombre_categoria, descripcion, tipo):
            nueva_categoria = Categoria(nombre_categoria, descripcion, tipo)
            nueva_categoria.agregar_categoria(self.lista_categorias)

    def eliminar_categoria(self, nombre_categoria):
            categoria = Categoria(nombre_categoria, "", "")
            categoria.eliminar_categoria(self.lista_categorias)

    def mostrar_categorias(self):
        if not self.lista_categorias:
            print("No hay categorías registradas.")
        else:
            print("Categorías registradas:")
            for categoria in self.lista_categorias:
                print(f"- {categoria.nombre_categoria} ({categoria.tipo})")
    
    def modificar_categoria(self, nombre_actual, nuevo_nombre, nueva_descripcion, nuevo_tipo):
        """Modifica una categoría existente por su nombre."""
        for categoria in self.lista_categorias:
            if categoria.nombre_categoria == nombre_actual:
                categoria.modificar_categoria(nuevo_nombre, nueva_descripcion, nuevo_tipo)
                return
        print(f"No se encontró la categoría '{nombre_actual}'.")
