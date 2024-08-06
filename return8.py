# Ejercicio 4: Devolver None Explícitamente o Implícitamente
# Descripción: Escribe una función llamada verificar_menor que tome dos números como 
# parámetros y devuelva True si el primer número es menor que el segundo, y None si
# ambos números son iguales.
def verificar_menor(primero,segundo):
    if primero < segundo:
        return True
    elif primero > segundo:
        return False
    else :
        return None
    
        
print(verificar_menor(7,9))
print(verificar_menor(10,9))
print(verificar_menor(17,17))
print(verificar_menor(17,17))
print(verificar_menor(17,17))


