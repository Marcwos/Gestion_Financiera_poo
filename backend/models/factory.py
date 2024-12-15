from models.inform_model import TransaccionIngreso, TransaccionGasto  

class TransaccionFactory:
    @staticmethod
    def crear_transaccion(tipo, monto, categoria, fecha, descripcion):
        if tipo not in ["Ingreso", "Gasto"]:
            raise ValueError("Tipo de transacción no válido") 
        if tipo == "Ingreso":
            return TransaccionIngreso(monto, categoria, fecha, descripcion)
        elif tipo == "Gasto":
            return TransaccionGasto(monto, categoria, fecha, descripcion)