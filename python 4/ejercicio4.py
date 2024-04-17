
lista = []

for i in range(5):
    while True:
        try: 
            numero = int(input("Ingrese un numero: "))

            if numero in lista:
                print ("¡El numero esta repetido!")
            else: 
                lista.append(numero)
                break
        except:
            print("Datos invalidos")
print (lista)
