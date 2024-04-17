
#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com


listaNumeros = []

for i in range (10):

    numero = int (input (f"Ingrese un numero entero: ") )
    listaNumeros.append (numero)

promedio= sum(listaNumeros)/10
maximo= max (listaNumeros)
minimo= min (listaNumeros)

print("El promedio de los numeros ingresados es: ", promedio)
print("El mayor de los numeros de la lista es:",maximo, "y el menor de los numeros de la lista es:",minimo)

   

