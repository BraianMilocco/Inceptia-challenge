import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity":[3,10,0,5]
})

def response_dict( available, attemps, max_attemps):
    return {
        "available": available,
        "attemps": attemps,
        "max_attemps": max_attemps,
        "attemps_left": max_attemps - attemps,
    }
def is_product_available(product_name, quantity, attemp=0):
    """Devuelve True si el producto esta disponible en la cantidad solicitada
    Se agrega una validacion para que la cantidad sea mayor a 0
    Se pasa a mayuscula el nombre del producto para evitar errores de tipeo
    Se agrega un contador de intentos para que el usuario no pueda intentar mas de 5 veces
    Se cambia el return por un diccionario para poder devolver la cantidad de intentos restantes"""
    if quantity < 1:
        return False
    max_attemps = 5
    if attemp >= max_attemps:
        return response_dict(False, attemp, max_attemps)
    df = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'].str.upper() == product_name.upper()]
    if df.empty or df['quantity'].iloc[0] < quantity:
        return response_dict(False, (attemp+1), max_attemps)
    return response_dict(True, attemp, max_attemps)


# En caso de que se quiera probar el codigo, descomentar las siguientes lineas

# if __name__ == "__main__":
#     product_name = input("Ingrese el nombre del producto: ")
#     quantity = int(input("Ingrese la cantidad del producto: "))
#     available = is_product_available(product_name, quantity)

#     if available["available"]:
#         print("El producto esta disponible")
#     attemps = available["attemps"]
#     while not available["available"]:
#         print("El producto no esta disponible, le quedan {} intentos".format(available["attemps_left"]))
#         product_name = input("Ingrese el nombre del producto: ")
#         quantity = int(input("Ingrese la cantidad del producto: "))
#         available = is_product_available(product_name, quantity, attemps)
#         attemps = available["attemps"]
#     if not available["available"]:
#         print("El producto no esta disponible")
#     else:
#         print("Gracias por su compra")