print ("ingrese la cantiad de segundos a convertir: ")

segundos = int (input())

dia = segundos // 86400

horas = (segundos % 86400)// 3600

minutos = ((segundos % 86400)% 3600) // 60

segundo= ((segundos % 86400)% 3600)% 60

print ("La cantidad de dias que equivalen es : ", dia)
print ("La cantidad de horas que equivalen es : ", horas)
print ("La cantidad de minutos que equivalen es : ", minutos)
print ("La cantidad de segundos que equivalen es : ", segundo)
