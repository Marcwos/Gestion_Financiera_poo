def eliminar_cuenta(usuario):
    nombre_cuenta = input("Ingrese el nombre de la cuenta a eliminar: ")
    usuario.eliminar_cuenta(nombre_cuenta)

# Mostrar cuentas
def mostrar_cuentas(usuario):
    usuario.mostrar_cuentas()