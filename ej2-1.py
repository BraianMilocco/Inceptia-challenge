import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity":[3,10,0,5]
})

def is_product_available(product_name, quantity):
    """Devuelve True si el producto esta disponible en la cantidad solicitada"""
    df = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'] == product_name]
    if df.empty or df['quantity'].iloc[0] < quantity:
        return False
    return True


""""Ejercicio 2.1: Refactorizado:
    - Se pasan los str a mayusculas para evitar errores de tipeo

def is_product_available(product_name, quantity):
    df = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'].str.upper() == product_name.upper()]
    if df.empty or df['quantity'].iloc[0] < quantity:
        return False
    return True
    
"""