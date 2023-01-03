# hoy_hace=12.00
# def mifunicon(nombre):
#     global hoy_hace
#     hoy_hace=50.00
#     print('hola',nombre,'la temperatura es de',hoy_hace)

# mifunicon('Andres')


def suma(*args):
    resultado=0
    for arg in args:
        resultado+=arg
    print(resultado)
suma(9,9,9,9)