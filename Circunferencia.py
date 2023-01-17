#Programa que imprime el area de una circunferencia
#El radio es ingresado por teclado
#El Càlculo se realiza con una funcion

import time
import math

def AreaCir(Radio):
	area=math.pi*Radio **2;
	return area 

radio=float(input("Ingresar radio de la circunferencia: "))
area=AreaCir(radio)
print("El area de la Circunferencia: ",area)

time.sleep(15)