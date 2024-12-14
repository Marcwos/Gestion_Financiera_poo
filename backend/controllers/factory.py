from controllers.transaction_controller import TransaccionIngreso, TransaccionGasto

class TransaccionFactory:
    @staticmethod
    def crear_transaccion(tipo, monto, categoria, fecha, descripcion):
        if tipo == "Ingreso":
            return TransaccionIngreso(monto, categoria, fecha, descripcion)
        elif tipo == "Gasto":
            return TransaccionGasto(monto, categoria, fecha, descripcion)
        else:
            raise ValueError("Tipo de transacción no válido")