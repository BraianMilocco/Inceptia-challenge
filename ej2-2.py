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
    """Devuelve True si el producto esta disponible en la cantidad solicitada"""
    max_attemps = 5
    if attemp >= max_attemps:
        return response_dict(False, attemp, max_attemps)
    df = _PRODUCT_DF.loc[_PRODUCT_DF['product_name'] == product_name]
    if df.empty or df['quantity'].iloc[0] < quantity:
        return False, (attemp + 1)
    return response_dict(True, attemp, max_attemps)

