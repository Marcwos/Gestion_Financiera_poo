from controllers.account_controller import Cuenta 

class Usuario:
    usuarios_registrados = []

    def __init__(self, nombre, email, password, saldo_actual=0, historial_transacciones=None):
        self.nombre = nombre
        self.email = email
        self.__password = password 
        self.__saldo_actual = saldo_actual 
        self.__historial_transacciones = historial_transacciones if historial_transacciones is not None else [] 
        self.__cuentas = [] 

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
        # Elimina una cuenta basada en el nombre de la cuenta
        for cuenta in self.cuentas:
            if cuenta.nombre_cuenta == nombre_cuenta:
                self.cuentas.remove(cuenta)
                print(f"Cuenta {nombre_cuenta} eliminada exitosamente.")
                return
        print(f"No se encontró la cuenta {nombre_cuenta}.")

    def mostrar_cuentas(self):
        if not self.cuentas:
            print(f"El usuario {self.nombre} no tiene cuentas.")
        else:
            print(f"Cuentas del usuario {self.nombre}:")
            for cuenta in self.cuentas:
                print(f"- {cuenta.nombre_cuenta} (Tipo: {cuenta.tipo_cuenta}, Saldo: {cuenta.saldo})")
