import re

lista = []
patron = "^[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ]+$"



for i in range (7):
    while True:
          nombre= input(f"Ingrese su nombre nombre: ")
          if re.search(patron,nombre):
                print ("El nombre ingresado es valido")
                lista.append(nombre)
                break
          else:
               print ("Carcteres incorrectos")

lista.sort()

print(lista)
