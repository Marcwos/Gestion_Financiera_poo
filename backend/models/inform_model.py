from models.transaction_model import TransaccionIngreso, TransaccionGasto  

class EstrategiaInforme:
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        raise NotImplementedError 

class EstrategiaInformeIngresos(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        transacciones_filtradas = [
            t for t in transacciones
            if fecha_inicio <= t.get_fecha() <= fecha_fin and isinstance(t, TransaccionIngreso)
        ]
        
        print(f"Transacciones filtradas (ingresos): {[t.get_monto() for t in transacciones_filtradas]}")

        total = sum(t.get_monto() for t in transacciones_filtradas)
        return f"Total de ingresos: {total}" 


class EstrategiaInformeGastos(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        transacciones_filtradas = [
            t for t in transacciones
            if fecha_inicio <= t.get_fecha() <= fecha_fin and isinstance(t, TransaccionGasto)
        ]
        
        print(f"Transacciones filtradas (gastos): {[t.get_monto() for t in transacciones_filtradas]}")

        total = sum(t.get_monto() for t in transacciones_filtradas)
        return f"Total de gastos: {total}"

class EstrategiaInformeNeto(EstrategiaInforme):
    def generar(self, transacciones, fecha_inicio, fecha_fin):
        # Filtrar las transacciones dentro del rango de fechas
        transacciones_filtradas = [
            t for t in transacciones if fecha_inicio <= t.get_fecha() <= fecha_fin
        ]

        ingresos = sum(t.get_monto() for t in transacciones_filtradas if isinstance(t, TransaccionIngreso))
        gastos = sum(t.get_monto() for t in transacciones_filtradas if isinstance(t, TransaccionGasto))
        neto = ingresos - gastos

        return f"Total neto: {neto}" 

class Informe:
    def __init__(self, estrategia: EstrategiaInforme):
        self.estrategia = estrategia

    def generar_informe(self, transacciones, fecha_inicio, fecha_fin):
        return self.estrategia.generar(transacciones, fecha_inicio, fecha_fin) 