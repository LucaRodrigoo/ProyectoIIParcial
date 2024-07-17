import datetime

class Utilidades:
    @staticmethod
    def calcular_edad(anio_nacimiento):
        anio_actual = datetime.datetime.now().year
        return anio_actual - anio_nacimiento
