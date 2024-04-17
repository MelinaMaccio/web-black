
#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com

lista = []
pares = []
suma = 0
print ("")

while suma < 100:
    valor=int(input("Ingrese un numero:"))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append (valor)
        suma +=valor 
cant = len (lista)

print(f"De un total de {cant} numeros ingresados, la suma de los numeros pares es {suma}")
print ("")


