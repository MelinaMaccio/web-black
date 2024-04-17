lado1 = float (input ("Ingrese el primer lado: "))
lado2 = float (input ("Ingrese el segundo lado: "))
lado3 = float (input ("Ingrese el tercer lado: "))

perimetro = lado1 + lado2 + lado3 

semip= perimetro/ 2

superficie= (semip*(semip- lado1)*(semip- lado2)*(semip-lado3))**0.5

print ("El valor del perimetro es: ", perimetro)

print ("El valor de la superficie es: ", superficie)


