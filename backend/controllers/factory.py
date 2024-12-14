class TransaccionFactory:
    @staticmethod
    def crear_transaccion(tipo, monto, categoria, fecha, descripcion):
        # abierto/cerrado - OCP
        if tipo not in ["Ingreso", "Gasto"]:
            raise ValueError("Tipo de transacción no válido")  # Manejo de errores

        # sustitución de Liskov - LSP
        if tipo == "Ingreso":
            return TransaccionIngreso(monto, categoria, fecha, descripcion)
        elif tipo == "Gasto":
            return TransaccionGasto(monto, categoria, fecha, descripcion)