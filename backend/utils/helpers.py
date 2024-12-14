from datetime import date, datetime

def validar_email(email):
    """Valida si el formato del email es correcto"""
    if "@" in email and "." in email:
        return True
    return False

def validar_password(password):
    """Valida si la contraseña cumple con un mínimo de longitud"""
    if len(password) >= 6:
        return True
    return False

def convertir_a_fecha(fecha_str):
    # Verificar si el parámetro es ya un objeto 'date'
    if isinstance(fecha_str, date):
        return fecha_str
    # Si es una cadena, convertirla a 'date'
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()