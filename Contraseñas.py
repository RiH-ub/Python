#Programa que permite verificar la contraseña 

#Mensaje de bienvenida 
import time
print("Hola RENZO")

#La contraseña es "cecilia"
ingreso = "cecilia"
dato = input("Introduzca su contraseña: ")


if ingreso == dato.lower():
	print("Contraseña correcta...!Ingresaste al Sistema!")#Si es correcto 
else:
    print("Contraseña incorrecta...!Acceso denegado!")#Si es incorrecto

time.sleep(10)		
