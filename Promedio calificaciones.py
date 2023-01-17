import time

print("**** SENATI ****")
print("PROGRAMA DE PROMEDIOS")

nombre=input("¿Cual es tu nombre?: ")
apellidos=input("¿Y tus Apellidos: ")
user=nombre +" "+ apellidos

Num1=float(input("Ingresar primer numero: "))
Num2=float(input("Ingresar segundo numero: "))
Num3=float(input("Promedio final: "))

Promedio_final=(Num1+Num2+Num3)/2

if Promedio_final <= 10.5:
   print("¡Lo sentimos, siga esforzándose!")
   
else:
   print("¡Felicidades",user,"estas aprovado!")

time.sleep(10)