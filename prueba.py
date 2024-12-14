from datetime import date

# Clases de Transacción para Ingreso y Gasto, adaptadas a tu código
class Transaccion:
    def __init__(self, monto, categoria, fecha, descripcion):
        self.__monto = monto
        self.__categoria = categoria
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


class TransaccionIngreso(Transaccion):
    def __init__(self, monto, categoria, fecha, descripcion):
        super().__init__(monto, categoria, fecha, descripcion)
        self.tipo_transaccion = "Ingreso"  # Definimos el tipo de transacción


class TransaccionGasto(Transaccion):
    def __init__(self, monto, categoria, fecha, descripcion):
        super().__init__(monto, categoria, fecha, descripcion)
        self.tipo_transaccion = "Gasto"  # Definimos el tipo de transacción


# Estrategias para generar informes
class EstrategiaInforme:
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        raise NotImplementedError


class EstrategiaInformeIngresos(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        # Convertir las fechas de entrada a tipo date
        fecha_inicio = convertir_a_fecha(fecha_inicio)
        fecha_fin = convertir_a_fecha(fecha_fin)

        # Filtrar transacciones dentro del rango de fechas
        transacciones_filtradas = [
            t for t in transacciones 
            if fecha_inicio <= t.get_fecha() <= fecha_fin and isinstance(t, TransaccionIngreso)
        ]
        
        # Depuración: Verificar las transacciones filtradas
        print(f"Transacciones filtradas (ingresos): {[t.get_monto() for t in transacciones_filtradas]}")

        total = sum(t.get_monto() for t in transacciones_filtradas)
        return f"Total de ingresos: {total}"


class EstrategiaInformeGastos(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        fecha_inicio = convertir_a_fecha(fecha_inicio)
        fecha_fin = convertir_a_fecha(fecha_fin)

        # Filtrar transacciones dentro del rango de fechas
        transacciones_filtradas = [
            t for t in transacciones 
            if fecha_inicio <= t.get_fecha() <= fecha_fin and isinstance(t, TransaccionGasto)
        ]
        
        # Depuración: Verificar las transacciones filtradas
        print(f"Transacciones filtradas (gastos): {[t.get_monto() for t in transacciones_filtradas]}")

        total = sum(t.get_monto() for t in transacciones_filtradas)
        return f"Total de gastos: {total}"


# Convertir la fecha desde formato string a tipo date
def convertir_a_fecha(fecha_str):
    return date.fromisoformat(fecha_str)


# Clase principal Informe que usa las estrategias
class Informe:
    def __init__(self, estrategia: EstrategiaInforme):
        self.estrategia = estrategia

    def generar_informe(self, transacciones, fecha_inicio, fecha_fin):
        return self.estrategia.generar(transacciones, fecha_inicio, fecha_fin)


# Función principal para prueba
def prueba_informes():
    # Crear transacciones de prueba
    lista_transacciones = [
        TransaccionIngreso(500, "Trabajo", date(2024, 12, 1), "Pago de salario"),
        TransaccionGasto(200, "Comida", date(2024, 12, 2), "Cena en restaurante"),
        TransaccionIngreso(300, "Freelance", date(2024, 12, 3), "Proyecto freelance"),
        TransaccionGasto(100, "Transporte", date(2024, 12, 4), "Taxi"),
        TransaccionIngreso(150, "Trabajo", date(2024, 12, 14), "Pago de salario extra"),
    ]
    
    # Imprimir lista de transacciones
    print("Lista de transacciones registradas:")
    for t in lista_transacciones:
        print(f"Tipo: {type(t).__name__}, Fecha: {t.get_fecha()}, Monto: {t.get_monto()}, Descripción: {t.get_descripcion()}")

    # Generar informe de ingresos
    estrategia_ingresos = EstrategiaInformeIngresos()
    informe_ingresos = Informe(estrategia_ingresos)
    resultado_ingresos = informe_ingresos.generar_informe(lista_transacciones, "2024-12-01", "2024-12-14")
    print("\n" + resultado_ingresos)

    # Generar informe de gastos
    estrategia_gastos = EstrategiaInformeGastos()
    informe_gastos = Informe(estrategia_gastos)
    resultado_gastos = informe_gastos.generar_informe(lista_transacciones, "2024-12-01", "2024-12-14")
    print("\n" + resultado_gastos)


# Ejecutar la prueba
if __name__ == "__main__":
    prueba_informes()
