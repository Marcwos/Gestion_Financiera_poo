from datetime import date

class MetaFinanciera:
    def __init__(self, id_meta, valor_objetivo, fecha_limite, descripcion):
        self.id_meta = id_meta
        self._descripcion = descripcion  
        self._valor_objetivo = valor_objetivo  
        self._fecha_limite = fecha_limite  

    def get_descripcion(self):
            return self._descripcion
    
    def calcular_progreso(self, cuenta):
        """Calcula el progreso en función de las transacciones de la cuenta."""
        progreso = 0
        for transaccion in cuenta.get_transacciones():
            if transaccion.get_categoria() == "ingreso":
                progreso += transaccion.get_monto()
        return progreso

    def verificar_cumplimiento(self, cuenta):
        """Verifica si la meta ha sido cumplida utilizando las transacciones de una cuenta."""
        progreso_actual = self.calcular_progreso(cuenta)

        if progreso_actual >= self._valor_objetivo:
            print(f"Meta '{self._descripcion}' cumplida. Progreso: {progreso_actual}/{self._valor_objetivo}")
        elif date.today() > self._fecha_limite:
            print(f"La fecha límite para la meta '{self._descripcion}' ha pasado. Progreso: {progreso_actual}/{self._valor_objetivo}")
        else:
            print(f"Progreso actual de la meta '{self._descripcion}': {progreso_actual}/{self._valor_objetivo}. La meta no se ha cumplido.")

    def registrar_meta(self, lista_metas):
        """Registra la meta en una lista de metas."""
        lista_metas.append(self)
        print(f"Meta '{self._descripcion}' registrada con éxito.")
