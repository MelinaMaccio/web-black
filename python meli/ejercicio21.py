#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com



frase=input("Ingrese una frase: ").lower()
vocales=0
for i in frase:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vocales+=1
print(f"En su frase hay {vocales} vocales")