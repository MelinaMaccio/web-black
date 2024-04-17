frase=input("Ingrese una frase: ")
palabras=0
for i in frase:
    if i==" ":
        palabras+=1
print(f"La frase tiene {palabras+1} palabras")