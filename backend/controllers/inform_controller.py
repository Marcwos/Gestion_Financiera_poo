
class Informe:
    def init(self, periodo_tiempo, tipo_informe):
        if tipo_informe not in ["ingreso", "gastos", "neto"]:
            raise ValueError(f"Tipo de informe '{tipo_informe}' no es válido.")

        self.periodo_tiempo = periodo_tiempo  # Periodo de tiempo podría utilizarse en una validación futura.
        self.tipo_informe = tipo_informe 

    def generar_informe(self, transacciones, fecha_inicio, fecha_fin):
        # Filtrar transacciones dentro del rango de fechas
        transacciones_filtradas = transacciones.consultar_transacciones_por_fecha(fecha_inicio, fecha_fin)

        # Generar el informe según el tipo
        if self.tipo_informe == "ingreso":
            informe = self._generar_informe_ingresos(transacciones_filtradas)
        elif self.tipo_informe == "gastos":
            informe = self._generar_informe_gastos(transacciones_filtradas)
        elif self.tipo_informe == "neto":
            informe = self._generar_informe_neto(transacciones_filtradas)

        return informe

    # Métodos privados para generar cada tipo de informe
    def _generar_informe_ingresos(self, transacciones):
        ingresos = [t for t in transacciones if t['tipo'] == 'ingreso']
        total = sum(t['monto'] for t in ingresos)
        return f"Total de ingresos: {total}"

    def _generar_informe_gastos(self, transacciones):
        gastos = [t for t in transacciones if t['tipo'] == 'gasto']
        total = sum(t['monto'] for t in gastos)
        return f"Total de gastos: {total}"

    def _generar_informe_neto(self, transacciones):
        ingresos = sum(t['monto'] for t in transacciones if t['tipo'] == 'ingreso')
        gastos = sum(t['monto'] for t in transacciones if t['tipo'] == 'gasto')
        neto = ingresos - gastos
        return f"Total neto: {neto}"