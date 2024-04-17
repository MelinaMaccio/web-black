while True:
        try: 
            edad = int (input ("Ingrese la edad de la persona a verificar: "))
             
            if 0 <= edad <= 110:
                if edad >= 65:
                     print ("La persona puede jubierlarse")
                     break
                else:
                     faltan = 65 - edad
                     print ("La persona no puede jubielarse, le faltan",faltan, "años")
                     break
            else:
                 print ("Edad invalida")
        except:
             print ("Sus datos ingresados son incorrectos")

                
 

