from datetime import datetime
import time

def restar_hora():
        formato = "%H:%M:%S"
        now=datetime.now()
        now=now.strftime(formato)
        h1 = datetime.strptime("19:00:00", formato)
        h2 = datetime.strptime(now, formato)
        if h2>h1:
            print("Te puedes ir a casa son mas de las 7")
        else:
            resultado = h1 - h2
            print("Aun Falta:", resultado, "Para Salir")

restar_hora()

