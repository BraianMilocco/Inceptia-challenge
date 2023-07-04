import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity":[3,10,0,5]
})

def is_product_available(product_name, quantity):
    """Devuelve True si el producto esta disponible en la cantidad solicitada
    Se agrega una validacion para que la cantidad sea mayor a 0
    Se pasa a mayuscula el nombre del producto para evitar errores de tipeo"""
    if quantity < 1:
        return False
    df = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'].str.upper() == product_name.upper()]
    if df.empty or df['quantity'].iloc[0] < quantity:
        return False
    return True


# En caso de que se quiera probar el codigo, descomentar las siguientes lineas

# if __name__ == "__main__":
#     product_name = input("Ingrese el nombre del producto: ")
#     quantity = int(input("Ingrese la cantidad del producto: "))
#     available = is_product_available(product_name, quantity)

#     if available:
#         print("El producto esta disponible")
#     if not available:
#         print("El producto no esta disponible")