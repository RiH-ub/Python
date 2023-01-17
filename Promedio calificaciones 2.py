import time
def prom():
	prom = (n1+n2+n3)/3
	print(f"El promedio de {n1}, {n2} y {n3} es: {prom}")
	return
n1=int(input("Ingresa su nota de GetConnect: "))
n2=int(input("Ingresa su nota de Emprendimiento: "))
n3=int(input("Ingresa su nota de Pythom: "))
prom()
prf=int(input("Ingresa el promedio obtenido: "))
if prf >10:
	print("Estas aprobado")
else:
	print("Estas desaprobado")

time.sleep(60)