from models.factory import TransaccionFactory
from controllers.category_controller import mostrar_categorias

def ingresar_transaccion(usuario, lista_transacciones, tipo_transaccion):
    descripcion = input(f"Ingrese la descripción del {tipo_transaccion.lower()}: ")
    monto = float(input(f"Ingrese el monto del {tipo_transaccion.lower()}: "))
    
    categoria = mostrar_categorias(usuario)
    if categoria is None:
        print("Categoría no válida. Transacción no registrada.")
        return
    
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    id_cuenta = input("Ingrese el ID de la cuenta: ")

    cuenta_encontrada = next((cuenta for cuenta in usuario.get_cuentas() if cuenta.get_id_cuenta() == id_cuenta), None)

    if cuenta_encontrada:
        transaccion = TransaccionFactory.crear_transaccion(tipo_transaccion, monto, categoria.nombre_categoria, fecha, descripcion)
        
        cuenta_encontrada.agregar_transaccion(transaccion)
        lista_transacciones.append(transaccion)

        print(f"{tipo_transaccion} registrado exitosamente.")
    else:
        print("La cuenta no existe.")

def ingresar_gastos(usuario, lista_transacciones):
    ingresar_transaccion(usuario, lista_transacciones, "Gasto")

def ingresar_ingresos(usuario, lista_transacciones):
    ingresar_transaccion(usuario, lista_transacciones, "Ingreso")