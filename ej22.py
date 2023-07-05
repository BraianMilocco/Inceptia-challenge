import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity":[3,10,0,5]
})

def response_dict( available, attempts, max_attempts):
    return {
        "available": available,
        "attempts": attempts,
        "max_attempts": max_attempts,
        "attempts_left": max_attempts - attempts,
    }
def is_product_available(product_name, quantity, attempt=0):
    """Devuelve True si el producto esta disponible en la cantidad solicitada
    Se agrega una validacion para que la cantidad sea mayor a 0
    Se pasa a mayuscula el nombre del producto para evitar errores de tipeo
    Se agrega un contador de intentos para que el usuario no pueda intentar mas de 5 veces
    Se cambia el return por un diccionario para poder devolver la cantidad de intentos restantes"""
    max_attempts = 5
    if attempt >= max_attempts:
        return response_dict(False, attempt, max_attempts)
    attempt = attempt + 1
    if quantity < 1:
        return response_dict(False, attempt, max_attempts)
    df = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'].str.upper() == product_name.upper()]
    if df.empty or df['quantity'].iloc[0] < quantity:
        return response_dict(False, attempt, max_attempts)
    return response_dict(True, attempt, max_attempts)


# En caso de que se quiera probar solo este ejercicio, descomentar las siguientes lineas

# if __name__ == "__main__":
#     product_name = input("Ingrese el nombre del producto: ")
#     quantity = int(input("Ingrese la cantidad del producto: "))
#     available = is_product_available(product_name, quantity)

#     if available["available"]:
#         print("El producto esta disponible")
#     attempts = available["attempts"]
#     while not available["available"]:
#         print("El producto no esta disponible, le quedan {} intentos".format(available["attempts_left"]))
#         product_name = input("Ingrese el nombre del producto: ")
#         quantity = int(input("Ingrese la cantidad del producto: "))
#         available = is_product_available(product_name, quantity, attempts)
#         attempts = available["attempts"]
#     if not available["available"]:
#         print("El producto no esta disponible")
#     else:
#         print("Gracias por su compra")