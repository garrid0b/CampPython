# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, 
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def inicializar(self,nombre,nota) :
        self.nombre=nombre
        self.nota=nota
    def Imprimir(self):
        print("Nombre del Alumno",self.nombre)
        print("Nota del Alumno",self.nota)
    def Aprobado(self):
        if self.nota>=10:
            print("El Alumno Aprobo el curso")
        else:
            print("El Alumno Reprobo el curso")

estudiante1=Alumno()
estudiante1.inicializar("Andres",7)
estudiante1.Imprimir()
estudiante1.Aprobado()
estudiante2=Alumno()
estudiante2.inicializar("Genesis",18)
estudiante2.Imprimir()
estudiante2.Aprobado()

