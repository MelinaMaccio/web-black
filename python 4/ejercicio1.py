
while True:
    try:
        edad= int (input ("Ingrese la edad de la persona: "))

        if 0 <= edad <= 120:
            if edad >= 18:
                print ("La persona es mayor de edad")
                break
            else:
                 print ("La persona es menor de edad")
                 break
        else:
              print ("La edad ingresada es invalida")

    
    except:
           print ("Ingrese datos validos")

