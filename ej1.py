import os
import requests
class GeoAPI:

    API_KEY = os.environ.get("API_KEY", "")
    LAT = os.environ.get("LAT", "")
    LON = os.environ.get("LON", "")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @classmethod
    def add_metric_param(cls):
        """Agrega el parametro units=metric a la url base de la API"""
        return f"{cls.BASE_URL}?units=metric"

    @classmethod
    def is_hot_in_pehuajo(cls):
        """Devuelve True si la temperatura actual en Pehuajo es mayor a 28 grados"""
        url = f'{cls.add_metric_param()}&lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}'

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return False

            return response.json()["main"]["temp"] > 28

        # Se pueden poner varios excepts para manejar distintos tipos de errores mas especificos
        except Exception as generic_exception:
            # aca se puede loguear el error
            return False


# En caso de que se quiera probar el codigo, descomentar las siguientes lineas

# if __name__ == "__main__":
#     print(GeoAPI.is_hot_in_pehuajo())
