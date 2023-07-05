from ej1 import GeoAPI
import time
from ej22 import is_product_available
from ej3 import validate_discount_code

"""Simula el comportamiento del Bot presentado en el diagrama de flujo de la consigna
Se utiliza el metodo is_product_available del ejercicio 22 para validar si el producto esta disponible
(permitiendo un maximo de 5 intentos hasta tirar una excepcion)
Se agrega un contador de intentos para que el usuario no pueda intentar mas de 5 veces un codigo de descuento
(se simula desde el mismo bot)
Se agrega un tiempo de espera para simular la espera de la respuesta del servidor
Se agrega un mensaje de confirmacion de pedido
Se agrega un mensaje de cancelacion de pedido en caso de que el usuario no ingrese un codigo de descuento valido
"""

if __name__ == "__main__":
    hot_in_pehuajo = GeoAPI.is_hot_in_pehuajo()
    if hot_in_pehuajo:
        print("Hace mas de 28 grados en Pehuajo")
    else:
        print("No hace mas de 28 grados en Pehuajo")
    tecla = input("Presione una tecla para continuar")
    product_name = input("Ingrese el nombre del producto: ")
    try:
        quantity = int(input("Ingrese la cantidad del producto: "))
    except ValueError:
        print("La cantidad debe ser un numero")
        exit()
    try:
        available = is_product_available(product_name, quantity)
        while not available:
            print("El producto no esta disponible, pruebe nuevamente")
            product_name = input("Ingrese el nombre del producto: ")
            try:
                quantity = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("La cantidad debe ser un numero")
                exit()
            available = is_product_available(product_name, quantity)
    except Exception as e:
        print("No tiene mas intentos")
        exit()
    print("El producto esta disponible")
    client_code = input("Ingrese el codigo de descuento: ")
    valid_code = validate_discount_code(client_code)
    attempts = 1
    while not valid_code and attempts < 5:
        ### Agrego los intentos para que se vea mas claro el funcionamiento y no se genere un loop infinito
        print(f"El descuento no es valido, le quedan {5 - attempts} intentos")
        client_code = input("Ingrese el codigo de descuento: ")
        valid_code = validate_discount_code(client_code)
        attempts += 1
    if not valid_code:
        print("El descuento no es valido, compra cancelada")
        exit()
    print("Espere ...")
    time.sleep(2)
    print("Descuento aplicado")
    print("Pedido Confirmado")
    exit()
