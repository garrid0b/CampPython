""" En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
Color
Ruedas
Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola. """

class Vehiculo:
    color="Amarillo"
    Ruedas=4
    Puertas=5
class Coche(Vehiculo):
    Velocidad=120
    Cilindrada=6

c=Coche()

print("Color del Vehiculo es",c.color,"Tiene",c.Ruedas,"Ruedas","Cantidad de puertas",
c.Puertas,"Viaja a una velocidad de",c.Velocidad, "y tiene", c.Cilindrada,"Cilindros")