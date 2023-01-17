#Programa en Pythom que imprime la suma de dos numeros
#El proceso es generado a travez de una funcion 
#Los números son ingresados por teclado
import time 

def calculo(num1,num2):
	rpta = num1 + num2
	print("la suma de los numeros es: ",rpta)

n1=float(input("Ingresar primer numero: "))
n2=float(input("Ingresar segundo numero: "))
calculo(n1,n2)

time.sleep(10)