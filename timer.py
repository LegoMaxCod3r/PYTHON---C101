#Importar la librería "Time"
import time

def countdown(seconds):

    while seconds > 0: #While (condicion):
        mins = int(seconds/60)
        secs = int(seconds%60)

        timer = f'{mins}:{secs} left'

        print(timer,end="\r")#Permite quedarse en la misma línea.
        time.sleep(1)

        seconds -= 1

    print(" ¡Se acabo el tiempo! ")


# Tiempo en segundos
seconds = input("Ingresa el tiempo en segundos: ")

countdown(int(seconds))