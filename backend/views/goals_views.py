from controllers.goals_finance_controller import MetaFinanciera

def menu_metas(usuario): 
    while True:
        print("\n=== GESTIÓN DE METAS ===")
        print("1. Agregar meta")
        print("2. Eliminar meta")
        print("3. Mostrar metas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la meta: ")
            monto = float(input("Ingrese el monto de la meta: "))
            fecha_limite = input("Ingrese la fecha límite (YYYY-MM-DD): ")
            meta = MetaFinanciera(descripcion, monto, fecha_limite)
            usuario.agregar_meta(meta)
            print("Meta agregada exitosamente.")
        elif opcion == '2':
            descripcion = input("Ingrese la descripción de la meta a eliminar: ")
            usuario.eliminar_meta(descripcion)
        elif opcion == '3':
            usuario.mostrar_metas()
        elif opcion == '4':
            print("Saliendo del menú de metas...")
            break
        else:
            print("Opción no válida.")
