class Cuenta:
    def __init__(self, id_cuenta, tipo_cuenta, nombre_cuenta, saldo_inicial=0):
        self.__id_cuenta = id_cuenta
        self.__tipo_cuenta = tipo_cuenta
        self.__nombre_cuenta = nombre_cuenta
        self.__saldo = saldo_inicial
        self.__transacciones = []  # Lista de transacciones asociadas

    # Métodos para obtener y configurar valores privados (cumple encapsulación)
    def get_id_cuenta(self):
        return self.__id_cuenta

    def get_tipo_cuenta(self):
        return self.__tipo_cuenta

    def set_tipo_cuenta(self, nuevo_tipo):
        self.__tipo_cuenta = nuevo_tipo

    def get_nombre_cuenta(self):
        return self.__nombre_cuenta

    def set_nombre_cuenta(self, nuevo_nombre):
        self.__nombre_cuenta = nuevo_nombre

    def get_saldo(self):
        return self.__saldo

    def get_transacciones(self):
        return self.__transacciones

    # Principio de Responsabilidad Única (SRP)
    def agregar_fondos(self, monto):
        if monto > 0:  # Validación simple
            self.__saldo += monto
            print(f"Se han agregado {monto} a la cuenta '{self.__nombre_cuenta}'. Saldo actual: {self.__saldo}")
        else:
            print("El monto a agregar debe ser mayor a 0.")

    def retirar_fondos(self, monto):
        if monto > self.__saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        else:
            self.__saldo -= monto
            print(f"Se han retirado {monto} de la cuenta '{self.__nombre_cuenta}'. Saldo actual: {self.__saldo}")

    # Principio de Abierto/Cerrado (OCP)
    def consultar_saldo(self):
        print(f"El saldo de la cuenta '{self.__nombre_cuenta}' es: {self.__saldo}")
        return self.__saldo

    # Principio de Inversión de Dependencias (DIP)
    def agregar_transaccion(self, transaccion):
        """
        Agrega una transacción a la cuenta.
        Se actualiza el saldo según el tipo de transacción.
        """
        if transaccion.tipo_transaccion not in ["Ingreso", "Gasto"]:
            print("Tipo de transacción no válido. Use 'Ingreso' o 'Gasto'.")
            return

        self.__transacciones.append(transaccion)
        if transaccion.tipo_transaccion == "Ingreso":
            self.agregar_fondos(transaccion.get_monto())
        elif transaccion.tipo_transaccion == "Gasto":
            self.retirar_fondos(transaccion.get_monto())
        print(f"Transacción '{transaccion.get_descripcion()}' añadida a la cuenta '{self.__nombre_cuenta}'.")

    def mostrar_transacciones(self):
        """
        Muestra todas las transacciones de la cuenta en orden.
        """
        if not self.__transacciones:
            print(f"La cuenta '{self.__nombre_cuenta}' no tiene transacciones.")
        else:
            print(f"Transacciones en la cuenta '{self.__nombre_cuenta}':")
            for transaccion in self.__transacciones:
                print(f"- {transaccion.descripcion}: {transaccion.monto} ({transaccion.tipo_transaccion})")
