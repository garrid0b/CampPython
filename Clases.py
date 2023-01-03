class Juguete:
    _encendido = True
    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido=False
    def QuitarOreja(self):
        pass
    def PonerOreja(self):
        pass
class potato(Juguete):
    pass
class Dino(Juguete):
    pass

p=Dino()
p.enciende()
print(p._encendido)
p.apaga()
print(p._encendido)


