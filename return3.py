# Ejercicio 3: Detener la Ejecución de la Función Tempranamente
# Descripción: Escribe una función llamada calificar que tome una 
# calificación numérica como parámetro y devuelva una cadena indicando 
# si la calificación es "Aprobado" (mayor o igual a 6) o "Reprobado" (menor a 6).
def calificar(nota):
    if nota >=6:
        return "Aprobado"
    else:
        return "Reprobado"
print(calificar(10))


