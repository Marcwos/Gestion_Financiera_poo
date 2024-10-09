class Cuenta:
    def __init__(self, id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial=0):
        self.id_cuenta = id_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.nombre_cuenta = nombre_cuenta
        self.saldo = saldo_inicial
        self.transacciones = []  # Relación de agregación 

    def agregar_fondos(self, monto):
        self.saldo += monto
        print(f"Se han agregado {monto} a la cuenta {self.nombre_cuenta}. Saldo actual: {self.saldo}")

    def retirar_fondos(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Se han retirado {monto} de la cuenta {self.nombre_cuenta}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        print(f"El saldo de la cuenta {self.nombre_cuenta} es: {self.saldo}")
        return self.saldo

    def agregar_transaccion(self, transaccion):
        """Agrega una transacción a la cuenta"""
        self.transacciones.append(transaccion)
        if transaccion.tipo_transaccion == "Ingreso":
            self.saldo += transaccion.monto
        elif transaccion.tipo_transaccion == "Gasto":
            self.saldo -= transaccion.monto
        print(f"Transacción '{transaccion.descripcion}' añadida a la cuenta {self.nombre_cuenta}.")

    def mostrar_transacciones(self):
        """Muestra todas las transacciones de la cuenta"""
        if not self.transacciones:
            print(f"La cuenta {self.nombre_cuenta} no tiene transacciones.")
        else:
            print(f"Transacciones en la cuenta {self.nombre_cuenta}:")
            for transaccion in self.transacciones:
                print(f"- {transaccion.descripcion}: {transaccion.monto} ({transaccion.tipo_transaccion})")
