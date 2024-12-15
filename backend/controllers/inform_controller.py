from models.inform_model import EstrategiaInformeGastos, EstrategiaInformeIngresos, EstrategiaInformeNeto
from datetime import datetime

def obtener_fechas():
    fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (YYYY-MM-DD): "), "%Y-%m-%d").date()
    fecha_fin = datetime.strptime(input("Ingrese la fecha de fin (YYYY-MM-DD): "), "%Y-%m-%d").date()
    return fecha_inicio, fecha_fin

def crear_estrategia(opcion):
    if opcion == '1':
        return EstrategiaInformeIngresos()
    elif opcion == '2':
        return EstrategiaInformeGastos()
    elif opcion == '3':
        return EstrategiaInformeNeto()