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
