#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com

num=input("Ingrese un numero: ")
palabra=""
for i in num:
    if i=="0":
        palabra+="cero "
    elif i=="1":
        palabra+="uno "
    elif i=="2":
        palabra+="dos "
    elif i=="3":
        palabra+="tres "
    elif i=="4":
        palabra+="cuatro "
    elif i=="5":
        palabra+="cinco "
    elif i=="6":
        palabra+="seis "
    elif i=="7":
        palabra+="siete "
    elif i=="8":
        palabra+="ocho "
    else:
        palabra+="nueve "
print(palabra)