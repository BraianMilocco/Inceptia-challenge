_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    """Valida que el codigo de descuento sea valido
    Aceptando hasta 3 caracteres de diferencia con los codigos disponibles"""
    set_code = set(discount_code)
    for code in _AVAILABLE_DISCOUNT_CODES:
        set_available_code = set(code)
        difference = set_code.symmetric_difference(set_available_code)
        if len(difference) <= 3:
            return True
    return False


# En caso de que se quiera probar el codigo, descomentar las siguientes lineas

# if __name__ == "__main__":
#     discount_code = input("Ingrese el codigo de descuento: ")
#     valid = validate_discount_code(discount_code)
#     if valid:
#         print("El codigo de descuento es valido")
#     else:
#         print("El codigo de descuento no es valido")