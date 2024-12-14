from datetime import date
from abc import ABC, abstractmethod

# Interfaz para las estrategias de cálculo de progreso
class EstrategiaProgreso(ABC):
    @abstractmethod
    def calcular_progreso(self, cuenta):
        """Método para calcular el progreso basado en las transacciones de la cuenta."""
        pass

# Estrategia para calcular el progreso basado en ingresos
class EstrategiaProgresoIngreso(EstrategiaProgreso):
    def calcular_progreso(self, cuenta):
        progreso = 0
        for transaccion in cuenta.get_transacciones():
            if transaccion.get_categoria() == "ingreso":
                progreso += transaccion.get_monto()
        return progreso

# Clase MetaFinanciera con el patrón de diseño Strategy
class MetaFinanciera:
    def __init__(self, id_meta, valor_objetivo, fecha_limite, descripcion, estrategia_progreso):
        self.id_meta = id_meta
        self._descripcion = descripcion  
        self._valor_objetivo = valor_objetivo  
        self._fecha_limite = fecha_limite  
        self.estrategia_progreso = estrategia_progreso  # DIP

    def get_descripcion(self):
        """Devuelve la descripción de la meta."""
        return self._descripcion  # SRP
    
    def verificar_cumplimiento(self, cuenta):
        """Verifica si la meta ha sido cumplida utilizando las transacciones de una cuenta."""
        progreso_actual = self.estrategia_progreso.calcular_progreso(cuenta)  # OCP

        # Verificar cumplimiento de la meta y condiciones de tiempo
        if progreso_actual >= self._valor_objetivo:
            print(f"Meta '{self._descripcion}' cumplida. Progreso: {progreso_actual}/{self._valor_objetivo}")
        elif date.today() > self._fecha_limite:
            print(f"La fecha límite para la meta '{self._descripcion}' ha pasado. Progreso: {progreso_actual}/{self._valor_objetivo}")
        else:
            print(f"Progreso actual de la meta '{self._descripcion}': {progreso_actual}/{self._valor_objetivo}. La meta no se ha cumplido.")

    def registrar_meta(self, lista_metas):
        """Registra la meta en una lista de metas."""
        lista_metas.append(self)  # SRP
        print(f"Meta '{self._descripcion}' registrada con éxito.")