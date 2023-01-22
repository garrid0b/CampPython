""" Crea un script que le pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas. """


paises= input("Agregar lista de paises (Separados por comas)")
lista=paises.split(",")
lista=set(lista)
lista=sorted(lista)
print(", ".join(lista))