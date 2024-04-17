
#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com

n = int (input("Ingrese un numero entero:"))

lista = []

while n != 0:
    lista.append(n)
    n= int(input("Ingrese un número : "))

maximo = max(lista)
minimo = min(lista)
cantidadDeElementos = len(lista)
promedio = sum(lista)/cantidadDeElementos
    

print ("El numero maximo es:", maximo, ". El minimo es:",minimo,".")

print ("El promedio entre todos ellos es:", promedio)

