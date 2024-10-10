from datetime import date

class MetaFinanciera:
    def init(self, id_meta, valor_objetivo, fecha_limite, descripcion):
        self.id_meta = id_meta
        self._descripcion = descripcion  # Este podría no ser privado, pero lo dejo opcional.
        self._valor_objetivo = valor_objetivo  # Atributo privado
        self._fecha_limite = fecha_limite  # Atributo privado
        self._valor_actual = 0  # Atributo privado

    def _actualizar_proceso(self, cantidad):  # Método privado
        """Actualiza el progreso de la meta."""
        self._valor_actual += cantidad
        print(f"Progreso actualizado: {self._valor_actual}/{self._valor_objetivo}")

    def verificar_cumplimiento(self):
        """Verifica si la meta ha sido cumplida o si ha pasado la fecha límite."""
        if self._valor_actual >= self._valor_objetivo:
            print("Meta cumplida.")
        elif date.today() > self._fecha_limite:
            print("La fecha límite ha pasado y la meta no se ha cumplido.")
        else:
            print("La meta no se ha cumplido.")

    def calcular_progreso(self, gestion_transacciones, fecha_inicio, fecha_fin):
        """Calcula el progreso basándose en las transacciones en un período dado."""
        transacciones = gestion_transacciones.consultar_transacciones_por_fecha(fecha_inicio, fecha_fin)
        for transaccion in transacciones:
            if transaccion.tipo_transaccion == "ingreso":
                self._actualizar_proceso(transaccion.monto)  # Uso del método privado