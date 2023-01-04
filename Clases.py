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
    color=""

    def __init__(self, nombre):
        self.color="verde"
        self.nombre=nombre

p=Dino("Andres")
print(p.color)
print(p.nombre)
class Proveedores:
    IdProveedor=0
    Nombre='Andres'
class Categorias:
    IdCategoria=0
    Nombre=""

class Productos:
    idproducto=0
    categoriaproducto=Categorias()
    precio=0
    tamaño=0
    TipodeProducto=0
    CIFproveedor=Proveedores()

produ=Productos()
produ.CIFproveedor.Nombre
produ.categoriaproducto.IdCategoria