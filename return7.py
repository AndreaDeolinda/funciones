# Descripción: Escribe una función llamada verificar_positivo que tome un número como 
# parámetro y devuelva "Positivo" si el número es mayor que 0, "Negativo" si el número
# es menor que 0, y "Cero" si el número es igual a 0.
def verificar_positivo(valor):
    if valor > 0:
        return "Positvo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Cero"
    
print(verificar_positivo(0))
print(verificar_positivo(10))
print(verificar_positivo(-12))
print(verificar_positivo(-1000))
print(verificar_positivo(-1000))