class Transaccion:
    def __init__(self, monto, categoria, fecha, descripcion):
        self.__monto = monto
        self.__categoria = categoria  # Relación de composición
        self.__fecha = fecha 
        self.__descripcion = descripcion
    
    def get_monto(self):
        return self.__monto

    def set_monto(self, nuevo_monto):
        self.__monto = nuevo_monto

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

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
            print(f"Transacción {id_transaccion} modificada.")
        else:
            print("Transacción no encontrada.")

    def eliminar_transaccion(self, id_transaccion, lista_transacciones):
        """Elimina una transacción por ID"""
        if 0 <= id_transaccion < len(lista_transacciones):
            lista_transacciones.pop(id_transaccion)
            print(f"Transacción {id_transaccion} eliminada.")
        else:
            print("Transacción no encontrada.")

    def consultar_transacciones_por_categoria(self, categoria, lista_transacciones):
        """Consulta todas las transacciones de una categoría"""
        transacciones_categoria = [t for t in lista_transacciones if t.get_categoria() == categoria]
        return transacciones_categoria

    def consultar_transacciones_por_fecha(self, fecha_inicio, fecha_fin, lista_transacciones):
        """Consulta todas las transacciones dentro de un rango de fechas"""
        transacciones_fecha = [
            t for t in lista_transacciones 
            if fecha_inicio <= t.get_fecha() <= fecha_fin
        ]
        return transacciones_fecha
    

class TransaccionIngreso(Transaccion):
    def __init__(self, monto, categoria, fecha, descripcion):
        super().__init__(monto, categoria, fecha, descripcion)
        # Aquí podrías agregar comportamiento o atributos adicionales para ingresos


class TransaccionGasto(Transaccion):
    def __init__(self, monto, categoria, fecha, descripcion):
        super().__init__(monto, categoria, fecha, descripcion)
        # Aquí podrías agregar comportamiento o atributos adicionales para gastos
