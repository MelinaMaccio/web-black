

nombre = input ("Ingrese un nombre y apellido: ")

numeros = ["0", "1","2","3","4","5","6","7","8","9"]

for letra in nombre:
    if letra in numeros:
        print ("El nombre tiene un numero, volver a ingresar")

