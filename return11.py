# Descripción: Escribe una función llamada factorial que tome un número como parámetro
# y devuelva su factorial.
result=1
def factorial(n):
    result=1
    for i in range(1,n+1):
     result *=i
    return result
    
print(factorial(5))
print(factorial(10))
print(factorial(7))
print(factorial(6))