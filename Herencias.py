import time

class Aves:
	def intro(self):
		print("Hay muchos tipos de aves")

	def vuelo(self):
		print("La mayoria de las aves pueden volar, pero algunas no")

class gorriones(Aves):
	def vuelo(self):
		print("Los gorriones pueden volar")

class avestruces(Aves):
	def vuelo(self):
		print("Los avestruces no pueden volar")

obj_aves = Aves()
obj_gorriones = gorriones()
obj_avestruces = avestruces()

obj_aves.intro()
obj_aves.vuelo()

obj_gorriones.intro()
obj_gorriones.vuelo()

obj_avestruces.intro()
obj_avestruces.vuelo()

time.sleep(50)