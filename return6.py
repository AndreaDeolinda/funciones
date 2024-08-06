# Escribe una función llamada calculos_avanzados que tome dos números como parámetros
# y devuelva la suma, la resta, la multiplicación 
# y la división de esos dos números.
def calculos_avanzados(primero,segundo):
    suma=primero+segundo
    resta=primero-segundo
    multiplicación=primero*segundo
    división=primero/segundo
    return suma, resta, multiplicación, división

print (calculos_avanzados(10,5))