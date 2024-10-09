from controllers.account_controller import Cuenta 

class Usuario:
    usuarios_registrados = []  # Lista para almacenar todos los usuarios

    def __init__(self, nombre, email, password, saldo_actual=0, historial_transacciones=None):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.saldo_actual = saldo_actual
        self.historial_transacciones = historial_transacciones if historial_transacciones is not None else []
        self.cuentas = []  # Lista para almacenar las instancias de cuentas del usuario

    def registrar_usuario(self):
        # Agrega el usuario actual a la lista de usuarios registrados
        Usuario.usuarios_registrados.append(self)
        print(f"Usuario {self.nombre} registrado exitosamente.")

    @classmethod
    def iniciar_sesion(cls, email, password):
        # Busca el usuario por email y verifica la contraseña
        for usuario in cls.usuarios_registrados:
            if usuario.email == email and usuario.password == password:
                print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}.")
                return usuario  # Retorna el objeto Usuario si las credenciales son correctas
        print("Email o contraseña incorrectos.")
        return None

    def agregar_cuenta(self, id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial=0):
        # Crea una instancia de Cuenta y la agrega a la lista de cuentas del usuario
        nueva_cuenta = Cuenta(id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
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
