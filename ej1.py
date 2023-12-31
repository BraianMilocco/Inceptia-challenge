import os
import requests
class GeoAPI:

    API_KEY = os.environ.get("API_KEY", "")
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    UNITS = "metric"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @classmethod
    def is_hot_in_pehuajo(cls):
        """Devuelve True si la temperatura actual en Pehuajo es mayor a 28 grados"""
        url = f'{cls.BASE_URL}?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units={cls.UNITS}'

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return False

            return response.json()["main"]["temp"] > 28

        # Se pueden poner varios excepts para manejar distintos tipos de errores mas especificos
        except Exception as generic_exception:
            # aca se puede loguear el error
            return False


# En caso de que se quiera probar solo este ejercicio, descomentar las siguientes lineas

# if __name__ == "__main__":
#     print(GeoAPI.is_hot_in_pehuajo())
