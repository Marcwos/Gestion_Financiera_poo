class Transaccion:
    def __init__(self, monto, tipo_transaccion, categoria, fecha, descripcion):
        self.monto = monto
        self.tipo_transaccion = tipo_transaccion  
        self.categoria = categoria
        self.fecha = fecha
        self.descripcion = descripcion
    
    def registrar_transaccion(self, lista_transacciones):
        """Registra la transacción en una lista"""
        lista_transacciones.append(self)
        print(f"Transacción registrada: {self.descripcion} - {self.monto} ({self.tipo_transaccion})")

    def consultar_transaccion(self, id_transaccion, lista_transacciones):
        """Busca y devuelve una transacción por ID"""
        if 0 <= id_transaccion < len(lista_transacciones):
            return lista_transacciones[id_transaccion]
        else:
            print("Transacción no encontrada.")

    def modificar_transaccion(self, id_transaccion, nuevos_datos, lista_transacciones):
        """Modifica una transacción con nuevos datos"""
        if 0 <= id_transaccion < len(lista_transacciones):
            transaccion = lista_transacciones[id_transaccion]
            transaccion.monto = nuevos_datos.get('monto', transaccion.monto)
            transaccion.tipo_transaccion = nuevos_datos.get('tipo_transaccion', transaccion.tipo_transaccion)
            transaccion.categoria = nuevos_datos.get('categoria', transaccion.categoria)
            transaccion.fecha = nuevos_datos.get('fecha', transaccion.fecha)
            transaccion.descripcion = nuevos_datos.get('descripcion', transaccion.descripcion)
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
        transacciones_categoria = [t for t in lista_transacciones if t.categoria == categoria]
        return transacciones_categoria

    def consultar_transacciones_por_fecha(self, fecha_inicio, fecha_fin, lista_transacciones):
        """Consulta todas las transacciones dentro de un rango de fechas"""
        transacciones_fecha = [
            t for t in lista_transacciones 
            if fecha_inicio <= t.fecha <= fecha_fin
        ]
        return transacciones_fecha

