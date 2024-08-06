# Ejercicio 4: Devolver None Explícitamente o Implícitamente
# Descripción: Escribe una función llamada es_mayor_de_edad que
# tome una edad como parámetro y devuelva True si la persona es
# mayor de edad (18 años o más). Si la edad es menor a 0, la función debería devolver None.
def es_mayor_de_edad(edad):
    if edad <= 0:
        return None
    elif edad >= 18:
     return True
    else:
        return False
    
print(es_mayor_de_edad(10))
print(es_mayor_de_edad(18))
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(-2))
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(0))
    