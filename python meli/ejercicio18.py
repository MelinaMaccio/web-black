#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com

DNI = []

n = int (input("Ingrese el DNI del cliente: "))

while n != -1:
    DNI.append(n)
    n = int (input("Ingrese el DNI del cliente: "))
cant=len(DNI)
prim=DNI[0]
ult=DNI [(cant-1)]

print ("El primer cliente es",prim, "y el ultimo clientes es" ,ult, "de un total de" ,cant, "cleintes") 
