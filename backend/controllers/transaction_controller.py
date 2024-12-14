from datetime import datetime

class Transaccion:
    def __init__(self, monto, categoria, fecha, descripcion):
        self.__monto = monto
        self.__categoria = categoria
        if isinstance(fecha, str):
            self.__fecha = datetime.strptime(fecha, "%Y-%m-%d").date()  # Convierte de str a date
        else:
            self.__fecha = fecha
        self.__descripcion = descripcion

    def get_monto(self):
        return self.__monto

    def get_categoria(self):
        return self.__categoria

    def get_fecha(self):
        return self.__fecha

    def get_descripcion(self):
        return self.__descripcion

    def registrar_transaccion(self, lista_transacciones):
        """Registra la transacción en una lista"""
        lista_transacciones.append(self)
        print(f"Transacción registrada: {self.__descripcion} - {self.__monto}")
        
    def consultar_transaccion(self, id_transaccion, lista_transacciones):
        """Busca y devuelve una transacción por ID"""
        if 0 <= id_transaccion < len(lista_transacciones):
            return lista_transacciones[id_transaccion]
        else:
            print("Transacción no encontrada.")
            return None

    def modificar_transaccion(self, id_transaccion, nuevos_datos, lista_transacciones):
        """Modifica una transacción con nuevos datos"""
        if 0 <= id_transaccion < len(lista_transacciones):
            transaccion = lista_transacciones[id_transaccion]
            transaccion.set_monto(nuevos_datos.get('monto', transaccion.get_monto()))
            transaccion.set_categoria(nuevos_datos.get('categoria', transaccion.get_categoria()))
            transaccion.set_fecha(nuevos_datos.get('fecha', transaccion.get_fecha()))
            transaccion.set_descripcion(nuevos_datos.get('descripcion', transaccion.get_descripcion()))
            print(f"Transacción modificada: {transaccion.get_descripcion()}")
        else:
            print("Transacción no encontrada.")


class TransaccionIngreso(Transaccion):
    def __init__(self, monto, categoria, fecha, descripcion):
        super().__init__(monto, categoria, fecha, descripcion)
        self.tipo_transaccion = "Ingreso"  # Definimos el tipo de transacción


class TransaccionGasto(Transaccion):
    def __init__(self, monto, categoria, fecha, descripcion):
        super().__init__(monto, categoria, fecha, descripcion)
        self.tipo_transaccion = "Gasto"  # Definimos el tipo de transacción
