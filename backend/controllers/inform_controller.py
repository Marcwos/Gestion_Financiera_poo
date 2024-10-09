from controllers.transaction_controller import Transaccion

class Informe:
    def __init__(self, periodo_tiempo, tipo_informe):
        self.periodo_tiempo = periodo_tiempo 
        self.tipo_informe = tipo_informe 

    def generar_informe(self, transacciones, fecha_inicio, fecha_fin):
       
        transacciones_filtradas = transacciones.consultar_transacciones_por_fecha(fecha_inicio, fecha_fin)

        if self.tipo_informe == "ingreso":
            informe = self.generar_informe_ingresos(transacciones_filtradas)
        elif self.tipo_informe == "gastos":
            informe = self.generar_informe_gastos(transacciones_filtradas)
        elif self.tipo_informe == "neto":
            informe = self.generar_informe_neto(transacciones_filtradas)
        return informe

    def generar_informe_ingresos(self, transacciones):
        ingresos = [t for t in transacciones if t['tipo'] == 'ingreso']
        total = sum(t['monto'] for t in ingresos)
        return f"Total de ingresos: {total}"
    def generar_informe_gastos(self, transacciones):
        gastos = [t for t in transacciones if t['tipo'] == 'gasto']
        total = sum(t['monto'] for t in gastos)
        return f"Total de gastos: {total}"
    def generar_informe_neto(self, transacciones):
        ingresos = sum(t['monto'] for t in transacciones if t['tipo'] == 'ingreso')
        gastos = sum(t['monto'] for t in transacciones if t['tipo'] == 'gasto')
        neto = ingresos - gastos
        return f"Total neto: {neto}"
