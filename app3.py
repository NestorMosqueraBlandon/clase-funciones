"""
Desarrolla una función llamada verificar_cumplimiento_normativas 
que tome tres parámetros: efluentes, residuos_peligrosos y consumo_agua. 
Estos parámetros son booleanos y representan si una industria cumple 
con las normativas ambientales en cuanto a efluentes,
 manejo de residuos peligrosos y consumo de agua, respectivamente.
   La función debe determinar si la industria cumple con las normativas
 ambientales. Se considera que la industria cumple con las normativas 
 si cumple al menos dos de los siguientes requisitos:

Tiene un sistema de tratamiento de efluentes instalado.
No genera residuos peligrosos o los maneja de manera adecuada.
Implementa medidas para la reducción del consumo de agua.
La función debe devolver una cadena de texto indicando si la industria cumple con las normativas ambientales: 'Cumple' o 'No Cumple'.
"""

def verificar_cumplimiento_normativas(efluentes, residuos_peligrosos, consumo_agua):
    if efluentes and residuos_peligrosos:
        return "Cumple"
    elif efluentes and consumo_agua:
        return "Comple"
    elif residuos_peligrosos and consumo_agua:
        return "Comple"
    else:
        return "No cumple"


google = verificar_cumplimiento_normativas(False, True, True)
print("Google: ", google)

meta = verificar_cumplimiento_normativas(True, True, True)
print("Meta: ", meta)

amd = verificar_cumplimiento_normativas(False, False, False)
print("AMD: ", amd)
