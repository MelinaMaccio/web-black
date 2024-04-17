#MELINA MACCIO
#D.S.I 6to B
# mechina4796@gmail.com

numero = int(input("Ingrese el número de la tabla de multiplicar que desea ver (entre 1 y 10): "))


if 1 <= numero <= 10:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("El número ingresado está fuera del rango permitido.")