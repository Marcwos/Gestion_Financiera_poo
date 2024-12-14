from controllers.transaction_controller import TransaccionIngreso, TransaccionGasto  
from utils.helpers import convertir_a_fecha

# Interfaz para estrategias de informes
class EstrategiaInforme:
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        raise NotImplementedError  # LSP

# Estrategia para generar informes de ingresos
class EstrategiaInformeIngresos(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        # Filtrar las transacciones de ingresos dentro del rango de fechas
        transacciones_filtradas = [
            t for t in transacciones
            if fecha_inicio <= t.get_fecha() <= fecha_fin and isinstance(t, TransaccionIngreso)
        ]
        
        # Ver qué transacciones fueron filtradas
        print(f"Transacciones filtradas (ingresos): {[t.get_monto() for t in transacciones_filtradas]}")

        total = sum(t.get_monto() for t in transacciones_filtradas)
        return f"Total de ingresos: {total}"  # SRP


# Estrategia para generar informes de gastos
class EstrategiaInformeGastos(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        # Filtrar las transacciones de gastos dentro del rango de fechas
        transacciones_filtradas = [
            t for t in transacciones
            if fecha_inicio <= t.get_fecha() <= fecha_fin and isinstance(t, TransaccionGasto)
        ]
        
        # Ver qué transacciones fueron filtradas
        print(f"Transacciones filtradas (gastos): {[t.get_monto() for t in transacciones_filtradas]}")

        total = sum(t.get_monto() for t in transacciones_filtradas)
        return f"Total de gastos: {total}"  # SRP


# Estrategia para generar informes netos
class EstrategiaInformeNeto(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        # Filtrar las transacciones dentro del rango de fechas
        transacciones_filtradas = [
            t for t in transacciones if fecha_inicio <= t.get_fecha() <= fecha_fin
        ]

        ingresos = sum(t.get_monto() for t in transacciones_filtradas if isinstance(t, TransaccionIngreso))
        gastos = sum(t.get_monto() for t in transacciones_filtradas if isinstance(t, TransaccionGasto))
        neto = ingresos - gastos

        return f"Total neto: {neto}"  # SRP


# Clase principal Informe que utiliza el patrón Strategy
class Informe:
    def __init__(self, estrategia: EstrategiaInforme):
        self.estrategia = estrategia  # DIP

    def generar_informe(self, transacciones, fecha_inicio, fecha_fin):
        return self.estrategia.generar(transacciones, fecha_inicio, fecha_fin)  # OCP