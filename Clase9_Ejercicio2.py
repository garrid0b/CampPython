# En este segundo ejercicio, 
# tenéis que crear una aplicación
# que obtendrá los elementos impares de una lista
# pasada por parámetro con filter y realizará una suma
# de todos estos elementos obtenidos mediante reduce.

from functools import reduce

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listab = list(filter(lambda x: x%2!=0,lista))
suma_lista = reduce(lambda x,y: x+y,listab)
print(listab)
print(suma_lista)