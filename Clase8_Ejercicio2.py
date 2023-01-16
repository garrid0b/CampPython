import pickle
class auto:
    modelo=''
    motor=0.0
    precio=0.0
    def __init__(self,modelo,motor,precio):
        self.modelo=modelo
        self.motor=motor
        self.precio=precio
    def __str__(self) -> str:
        return f'El Coche {self.modelo} con motor {self.motor} tiene un precio de {self.precio}'
    def getmodelo(self):
        return self.modelo
    def getmotor(self):
        return self.motor
    def getprecio(self):
        return self.precio

def guardar():
    f=open('datos.bin','wb')
    pickle.dump(vehiculo,f)
    f.close

def abrir():
    f=open('datos.bin','rb')
    recuperardatos=pickle.load(f)
    f.close()
    return recuperardatos

vehiculo=auto('Hyundai',1.2,11900.00)
guardar()
vehiculo2=abrir()
print(str(vehiculo2))