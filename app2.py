"""
Desarrolla una función llamada evaluar_contaminacion_suelo que tome tres parámetros: 
metales_pesados, hidrocarburos y plaguicidas. Estos parámetros son booleanos y representan
 la presencia o ausencia de metales pesados, hidrocarburos y plaguicidas en una muestra de suelo,
   respectivamente. 
   
   La función debe determinar si la contaminación del suelo es preocupante o no. 
   Se considera que la contaminación es preocupante si hay presencia de metales pesados o 
   hidrocarburos, o si hay presencia de plaguicidas. Si ninguno de estos contaminantes está presente, 
   se considera que la contaminación del suelo no es preocupante. La función debe devolver una cadena 
   de texto indicando el estado de la contaminación del suelo: 'Preocupante' o 'No preocupante'.
"""
# Booleano => False O True


def evaluar_contaminacion_suelo(metales_pesados, hidrocarburos, plaguicidas):
    if metales_pesados == True or hidrocarburos == True or plaguicidas == True:
        return "Preocupante"
    else:
        return "No preocupante"
    
rio_quito = evaluar_contaminacion_suelo(False, True, False)
print("Rio Quito: ", rio_quito)

rio_medellin = evaluar_contaminacion_suelo(False, False, False)
print("Rio Medellin: ", rio_medellin)

rio_tado = evaluar_contaminacion_suelo(True, True, True)
print("Rio Tado: ", rio_tado)
