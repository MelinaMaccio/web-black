frase=input("Ingrese una frase: ").lower()
vocales=0
consonantes=0
for  i in frase:
    if i==" ":
        continue
    elif i=="a" or i=="á" or i=="e" or  i=="é" or  i=="i" or  i=="í" or i=="o" or i=="ó" or i=="u" or i=="ú":
        vocales+=1
    else:
        consonantes+=1
print(f"La frase tiene {vocales} vocales y {consonantes} consonantes")