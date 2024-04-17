# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Determinar la cantidad de letras que tiene la palabra
cantidad_letras = len(palabra)

# Mostrar la cantidad de letras que tiene la palabra
print("La palabra ingresada tiene", cantidad_letras, "letras.")

# Verificar si la palabra termina en vocal
ultima_letra = palabra[-1]
if ultima_letra in 'aeiouAEIOU':
    print("La palabra termina en vocal.")
else:
    print("La palabra no termina en vocal.")