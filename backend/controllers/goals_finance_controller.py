from datetime import date

class MetaFinanciera:
    def __init__(self, id_meta, valor_objetivo, fecha_limite, descripcion):
        self.id_meta = id_meta
        self.descripcion = descripcion
        self.valor_objetivo = valor_objetivo
        self.fecha_limite = fecha_limite
        self.valor_actual = 0

    def actualizar_proceso(self, cantidad):
        self.valor_actual += cantidad
        print(f"rogreso actualizado: {self.valor_actual}/{self.valor_objetivo}")

    def verificar_cumplimiento(self):
        if self.valor_actual >= self.valor_objetivo:
            print("Met cumplida.")
        elif date.today() > self.fecha_limite:
            print("La fecha limite ha pasado y la meta no se ha cumplido.")
        else:
            print("La meta no se ha cumplido.")

    def calcular_progreso(self, gestion_transacciones, fecha_inicio, fecha_fin):
        transacciones = gestion_transacciones.consultar_transacciones_por_fecha(fecha_inicio, fecha_fin)
        for transaccion in transacciones:
            if transaccion.tipo_transaccion == "ingreso":
                self.actualizar_proceso(transaccion.monto)
