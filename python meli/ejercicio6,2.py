# Solicitar al usuario que ingrese las medidas de frente y fondo del terreno
frente = float(input("Ingrese la medida de frente del terreno: "))
fondo = float(input("Ingrese la medida de fondo del terreno: "))

# Determinar si el terreno es cuadrado o rectangular
if frente == fondo:
    print("El terreno es cuadrado.")
    forma = "cuadrado"
else:
    print("El terreno es rectangular.")
    forma = "rectangular"

# Calcular la superficie del terreno
superficie = frente * fondo

# Mostrar la superficie del terreno
print("La superficie del terreno", forma, "es:", superficie)