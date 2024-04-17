email=input("Ingrese su email: ")
valido=0
for i in email:
    if i=="@":
        valido+=1
if len(email)<255:
    valido+=1
if valido==2:
    print("El mail es correcto. ")
else:
    print("El mail es incorrecto")