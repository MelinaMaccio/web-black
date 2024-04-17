a=float(input("Ingrese coeficiente A: "))
b=float(input("Ingrese coeficiente B: "))
c=float(input("Ingrese coeficiente C: "))

discriminante=(b**2)-4*a*c
if discriminante<0:
    print("Las raices son complejas")
elif discriminante>0:
    x1=(-b+discriminante**.5)/(2*a)
    x2=(-b-discriminante**.5)/(2*a)
    print(f"El polinomio tiene 2 raices: {x1} y {x2}")
else:
    x=-b/(2*a)
    print(f"La raiz del polinomio es {x}")