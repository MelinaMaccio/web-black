#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com

import random
num=random.randrange(0,100)
while True:
    op=int(input("Ingrese un nume entero entre 0 y 100: "))
    if op<num:
        print("El numero aleatorio es mayor al numero que ingresaste.")
    elif op>num:
        print("El numero aleatorio es menor al numero que ingresaste.")
    else:
        print(" Adivino el numero")
        break