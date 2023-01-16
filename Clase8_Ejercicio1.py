def crear():
    f= open('archivo.txt','x')
    f.write('Archivo Creado \n')
    f.close()

def abrir():
    f=open('archivo.txt','a')
    f.write('agregando lineas adicionales\n')
    f.write('parte de abrir nuevamente el archivo del ejercicio.\n')
    f.close()

if __name__ == '__main__':
    try:
        crear()
    except FileExistsError:
        print('El Archivo ya fue creado.')
    abrir()
