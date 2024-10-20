from controllers.transaction_controller import TransaccionIngreso, TransaccionGasto  

class Informe:
    def __init__(self, tipo_informe):  # Constructor correcto
        if tipo_informe not in ["ingreso", "gastos", "neto"]:
            raise ValueError(f"Tipo de informe '{tipo_informe}' no es válido.")
        self.tipo_informe = tipo_informe

    def generar_informe(self, transacciones, fecha_inicio, fecha_fin):
        # Filtrar transacciones dentro del rango de fechas
        transacciones_filtradas = [t for t in transacciones if fecha_inicio <= t.get_fecha() <= fecha_fin]
        
        # Generar el informe según el tipo
        if self.tipo_informe == "ingreso":
            return self._generar_informe_ingresos(transacciones_filtradas)
        elif self.tipo_informe == "gastos":
            return self._generar_informe_gastos(transacciones_filtradas)
        elif self.tipo_informe == "neto":
            return self._generar_informe_neto(transacciones_filtradas)

    def _generar_informe_ingresos(self, transacciones):
        # Filtrar ingresos
        ingresos = [t for t in transacciones if isinstance(t, TransaccionIngreso)]
        total = sum(t.get_monto() for t in ingresos)
        return f"Total de ingresos: {total}"

    def _generar_informe_gastos(self, transacciones):
        # Filtrar gastos
        gastos = [t for t in transacciones if isinstance(t, TransaccionGasto)]
        total = sum(t.get_monto() for t in gastos)
        return f"Total de gastos: {total}"

    def _generar_informe_neto(self, transacciones):
        ingresos = sum(t.get_monto() for t in transacciones if isinstance(t, TransaccionIngreso))
        gastos = sum(t.get_monto() for t in transacciones if isinstance(t, TransaccionGasto))
        neto = ingresos - gastos
        return f"Total neto: {neto}"
