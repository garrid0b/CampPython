# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros),
#  calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# (Tu índice de masa corporal es donde es el índice de masa corporal) calculado redondeado con dos decimales. 
# Tienes que subir capturas de pantalla en una carpeta comprimida zip.

print('Hola, por favor ingresa tu estatura en Metros')
estatura=input()
estatura=float(estatura)
print('por favor ingresa tu peso en KG')
peso=input()
peso=float(peso)
masa=peso/estatura
print(f'Tu índice de masa corporal es donde es {round(masa,2)}')
