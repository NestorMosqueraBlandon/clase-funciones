#float es un numero de coma flotante es decir un numero decimal

"""
    Esta función calcula un índice de calidad del aire basado en los niveles
    de PM10, SO2 y NO2.

    La función RECIBE los siguientes ARGUMENTOS:
    pm10 (float): Nivel de partículas PM10 en microgramos por metro cúbico.
    so2 (float): Nivel de dióxido de azufre en microgramos por metro cúbico.
    no2 (float): Nivel de dióxido de nitrógeno en microgramos por metro cúbico.

    La funcion retorna :
    str: El índice de calidad del aire, que puede ser "Bueno", "Moderado", "No saludable para grupos sensibles",
    "No saludable", "Muy no saludable" o "Peligroso".
"""

def calcular_indice_calidad_aire(pm10, so2, no2):
    
    indice = ""
    max_pm10 = 50
    max_so2 = 20
    max_no2 = 40

    if pm10 <= max_pm10 and so2 <= max_so2 and no2 <= max_no2:
        indice = "Bueno"
    elif pm10 <= 100 and so2 <= 50 and no2 <= 100:
        indice = "Moderado"
    elif pm10 <= 150 and so2 <= 100 and no2 <= 200:
        indice = "No saludable para grupos sensibles"
    elif pm10 <= 100 and so2 <= 200 and no2 <= 400:
        indice = "No saludable"
    elif pm10 <= 300 and so2 <= 400 and no2 <= 800:
        indice = "Muy no saludable"
    else:
        indice = "Peligroso"
    
    return indice


#Datos ciudad Medellin
medellin = calcular_indice_calidad_aire(55, 3.45, 6.7655)
print("Medellin: ", medellin)


#Datos ciudad Bogota
bogota = calcular_indice_calidad_aire(100.4, 4.5, 9.755)
print("Bogota: ", bogota)


#Datos ciudad Cali
cali = calcular_indice_calidad_aire(2.5, 5, 9.755)
print("Cali: ", cali)


#Datos ciudad  Barranquilla
barranquilla = calcular_indice_calidad_aire(500, 10000, 9005)
print("Barranquilla: ", barranquilla)