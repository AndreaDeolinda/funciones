# Ejercicio 5: Contar palabras en una cadena
# Descripción: Escribe una función llamada contar_palabras que tome una cadena de texto como 
# parámetro y devuelva el número de palabras en la cadena.
def contar_palabras(cadena):
    palabras=cadena.split() #cuenta el espacio que hay entre palabras

    return len(palabras) #devuelve el numero de palabras usando Len
cadena_de_prueba="Me imagino que tuviste un día cansado en la fabrica."
resultado=(contar_palabras(cadena_de_prueba))
print(resultado)
cadena_de_prueba="Como te llamas?."
resultado=(contar_palabras(cadena_de_prueba))
print(resultado)
cadena_de_prueba="Cual es tu color favorito "
resultado=(contar_palabras(cadena_de_prueba))
print(resultado)