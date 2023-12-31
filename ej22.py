import pandas as pd

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class AttemptsManager(metaclass=Singleton):
    """Singleton para poder controlar la cantidad de intentos de un usuario
    En un caso mas complejo dentro de un servidor se podrian guardar diccionarios de attempts que se borren cada
    cierto tiempo para mejorar la performance y no tener que guardar todos los intentos de todos los usuarios"""
    def __init__(self):
        self.attempts = 0
        self.max_attempts = 5

    def add_attempt(self):
        self.attempts += 1

    def get_attempts(self):
        return self.attempts

    def reset_attempts(self):
        self.attempts = 0

    def has_attempts(self):
        return self.attempts < self.max_attempts

def validate_attempts(func):
    """Decorador para validar la cantidad de intentos de un usuario"""
    def wrapper(*args, **kwargs):
        attempts_manager = AttemptsManager()
        if not attempts_manager.has_attempts():
            raise Exception("No tiene más intentos")
        attempts_manager.add_attempt()
        result = func(*args, **kwargs)
        if result:
            attempts_manager.reset_attempts()
        return result
    return wrapper

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity":[3,10,0,5]
})

@validate_attempts
def is_product_available(product_name, quantity):
    """Devuelve True si el producto esta disponible en la cantidad solicitada
    Se agregar un decorador para validar la cantidad de intentos del usuario
    y evitar un posible loop infinito, sin modificar la logica de la funcion"""
    if quantity < 1:
        return False
    product = _PRODUCT_DF.loc[
        (_PRODUCT_DF['product_name'].str.upper() == product_name.upper()) &
        (_PRODUCT_DF['quantity'] >= quantity)
    ]
    return not product.empty



# En caso de que se quiera probar solo este ejercicio, descomentar las siguientes lineas

# if __name__ == "__main__":
#     product_name = input("Ingrese el nombre del producto: ")
#     quantity = int(input("Ingrese la cantidad del producto: "))
#     try:
#         available = is_product_available(product_name, quantity)
#         while not available:
#             print("El producto no esta disponible, pruebe nuevamente")
#             product_name = input("Ingrese el nombre del producto: ")
#             quantity = int(input("Ingrese la cantidad del producto: "))
#             available = is_product_available(product_name, quantity)
#         print("El producto esta disponible")
#     except Exception as e:
#         print(e)
#         print("No tiene mas intentos")
#         exit()
