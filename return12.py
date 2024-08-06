# Ejercicio 4: Números pares en una lista
# Descripción: Escribe una función llamada numeros_pares que tome una lista de números
# como parámetro y devuelva una lista de solo los números pares.
def numeros_pares(lista):
   pares=[]
   for numero in lista: #numero saca el numero almacenado en la lista en cada iteración
      if numero % 2 == 0:
         pares.append(numero)
   return pares

lista=[1,3,7,9,41,1,2,4,6] 
print(numeros_pares(lista))
lista=[1,2,3,5,7,56,12,40,30,29] 
print(numeros_pares(lista))
lista=[1,3,7,9,] 
print(numeros_pares(lista))

