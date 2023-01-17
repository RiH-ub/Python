# Nombre
print("Primero quiero saber mas sobre ti")
nom = input("Dime tu nombre: ")
ape = input("Dime tu apellido: ")

user = nom + " " + ape

# Bienvenida
print()
print("Te dire tu peso ideal,",user,)

# Datos
estatura = float(input("Dime tu estatura en cm: "))
peso = float(input("Dime tu peso en kg: "))

# Formula del IMC
imc = ( peso / ((estatura / 100) ** 2))

# Reduccion de decimales
final = format(imc, ".2f")  #Dos filas (".2f")

# Resultado
print()
print("Tu IMC es: "+ final)

# Condiciones
if imc <= 18.5:
  print("¡Estas flac@, come mas, "+user+"!")

elif imc <= 24.9:
  print("¡Bien hecho, "+user+", tienes un peso saludable!")

elif imc <= 29.9:
  print("¡Tienes sobre peso "+user+", intenta bajarle a la comida!")

else:
  print("¡Tienes obesidad, "+user+" AAHHHH!")

# Mensaje final
print()
print("Programa finalizado. ¡Hasta luego!")

time.sleep(10)