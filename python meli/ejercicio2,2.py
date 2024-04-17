# Definir un diccionario con los nombres de los meses
meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

# Pedir al usuario que ingrese un número de mes
numero_mes = int(input("Ingrese un número de mes (1-12): "))

# Verificar si el número de mes es válido y mostrar el nombre del mes correspondiente
if numero_mes in meses:
    nombre_mes = meses[numero_mes]
    print("El mes correspondiente al número", numero_mes, "es", nombre_mes)
else:
    print("Número de mes inválido. Por favor, ingrese un número entre 1 y 12.")