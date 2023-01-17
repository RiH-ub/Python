# Pide al usuario que ingrese su frecuencia cardíaca
heart_rate = int(input("Ingresa tu frecuencia cardíaca: "))

# Determina la edad del usuario
age = int(input("Ingresa tu edad: "))

# Determina el género del usuario
gender = input("Ingresa tu género (M para masculino, F para femenino): ")

# Determina el rango normal de frecuencia cardíaca para la edad y género del usuario
if gender == 'M':
  if age >= 18 and age <= 25:
    normal_range = (60, 100)
  elif age >= 26 and age <= 35:
    normal_range = (70, 100)
  elif age >= 36 and age <= 45:
    normal_range = (70, 110)
  elif age >= 46 and age <= 55:
    normal_range = (70, 120)
  elif age >= 56 and age <= 65:
    normal_range = (70, 130)
  elif age >= 66 and age <= 75:
    normal_range = (70, 140)
  elif age >= 76:
    normal_range = (70, 150)
else:
  if age >= 18 and age <= 25:
    normal_range = (60, 100)
  elif age >= 26 and age <= 35:
    normal_range = (70, 100)
  elif age >= 36 and age <= 45:
    normal_range = (70, 110)
  elif age >= 46 and age <= 55:
    normal_range = (70, 120)
  elif age >= 56 and age <= 65:
    normal_range = (70, 130)
  elif age >= 66 and age <= 75:
    normal_range = (70, 140)
  elif age >= 76:
    normal_range = (70, 150)

# Compara la frecuencia cardíaca del usuario con el rango normal
if heart_rate < normal_range[0]:
  print("Tu frecuencia cardíaca es muy baja.")
elif heart_rate > normal_range[1]:
  print("Tu frecuencia cardíaca es muy alta.")
else:
  print("Tu frecuencia cardíaca es normal.")

