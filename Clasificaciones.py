import time

class Alumnos:
	def inicializar(self,nom,ape,cur,prom):
		self.nombre=nom
		self.apellido=ape
		self.curso=cur
		self.promedio=prom

	def imprimir(self):
		print("Nombre:",self.nombre)
		print("Apellido:",self.apellido)
		print("Curso:",self.curso)
		print("Promedio:",self.promedio)
		print()

alumno1=Alumnos()
alumno1.inicializar("Angelo Marcell","Díaz Silva","Lenguaje",18)
alumno1.imprimir()

alumno2=Alumnos()
alumno2.inicializar("Elena","Silva Grandez","Ingles",13)
alumno2.imprimir()

alumno3=Alumnos()
alumno3.inicializar("Renzo Zahír","Díz Silva","Matemáticas",12)
alumno3.imprimir()


time.sleep(20)