# Definir variables
igv = float()

mnto = float()

totalfac = float()

imp = float()

op = str()

des = str()

alm = str()

cn = str()

igv = 0.18




import time

while True:

 # Ingresar y procesar datos
 print("|   RESTAURANTE S.A | | MENÚ   |")

 print("                                ")

 print("| A |        DESAYUNO          |")

 print("| B |        ALMUERZO          |")

 print("| C |          CENA            |")

 print("| D |========= SALIR ==========|")

 while True:

  op = input()

  op = str.lower(op)

  if not (op=="a" or op=="b" or op=="c" or op=="d"):

   print("Entrada inválida")

  if (op=="a" or op=="b" or op=="c" or op=="d"): break

 if op=="a":

  print("|            Desayuno          |")

  print("| A |Papa rellena       |S/4.50|")

  print("| B |Chaufa             |S/5.00|")

  print("| C |Juane de gallina   |S/9.00|")

  print("| D |Jugo de Papaya     |S/8.00|")

  print("| E |Pan con Pollo      |S/7.00|")

  print("| F |Pan con Jamón      |S/7.00|")

  print("| G |Pan con Tortilla   |S/7.00|")

  print("| J |========== SALIR =========|")

  while True:

   des = input()

   des = str.lower(des)

   if not (des=="a" or des=="b" or des=="c" or des=="d" or des=="e" or des=="f" or des=="g" or des=="j"):

    print("Entrada inválida")

   if (des=="a" or des=="b" or des=="c" or des=="d" or des=="e" or des=="f" or des=="g" or des=="j"): break

  if des=="a":

   mnto = 4.50

   imp = mnto*igv

   totalfac = mnto+imp

  elif des=="b":

   mnto = 5.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif des=="c":

   mnto = 9.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif des=="d":

   mnto = 8.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif des=="e":

   mnto = 7.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif des=="f":

   mnto = 7.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif des=="g":

   mnto = 7.00

   imp = mnto*igv

   totalfac = mnto+imp

 elif op=="b":

  print("|            Almuerzo          |")

  print("| A |Tallarines verdes |S/4.50 |")

  print("| B |Aji de gallina    |S/5.00 |")

  print("| C |Chicharrón        |S/9.00 |")

  print("| D |Arroz con pollo   |S/8.00 |")

  print("| E |Tallarines rojos  |S/7.00 |")

  print("| F |Inchicapi         |S/7.00 |")

  print("| G |Sudado de pollo   |S/7.00 |")

  print("| J |========= SALIR ==========|")

  while True:

   alm = input()

   alm = str.lower(alm)

   if not (alm=="a" or alm=="b" or alm=="c" or alm=="d" or alm=="e" or alm=="f" or alm=="g" or alm=="j"):

    print("Entrada inválida")

   if (alm=="a" or alm=="b" or alm=="c" or alm=="d" or alm=="e" or alm=="f" or alm=="g" or alm=="j"): break

  if alm=="a":

   mnto = 4.50

   imp = mnto*igv

   totalfac = mnto+imp

  elif alm=="b":

   mnto = 5.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif alm=="c":

   mnto = 9.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif alm=="d":

   mnto = 8.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif alm=="e":

   mnto = 7.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif alm=="f":

   mnto = 7.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif alm=="g":

   mnto = 7.00

   imp = mnto*igv

   totalfac = mnto+imp

 elif op=="c":

  print("|             Cena             |")

  print("| A |Pizza Exprés       |S/9.50|")

  print("| B |Ensalada Campera   |S/7.50|")

  print("| C |Gazpacho           |S/6.00|")

  print("| D |Caldo de Gallina   |S/6.00|")

  print("| E |Pollo al horno     |S/5.50|")

  print("| F |Menestrón          |S/4.00|")

  print("| G |========== SALIR =========|")

  while True:

   cn = input()

   cn = str.lower(cn)

   if not (cn=="a" or cn=="b" or cn=="c" or cn=="d" or cn=="e" or cn=="f" or cn=="g"):

    print("Entrada inválida")

   if (cn=="a" or cn=="b" or cn=="c" or cn=="d" or cn=="e" or cn=="f" or cn=="g"): break

  if cn=="a":

   mnto = 9.50

   imp = mnto*igv

   totalfac = mnto+imp

  elif cn=="b":

   mnto = 7.50

   imp = mnto*igv

   totalfac = mnto+imp

  elif cn=="c":

   mnto = 6.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif cn=="d":

   mnto = 6.00

   imp = mnto*igv

   totalfac = mnto+imp

  elif cn=="e":

   mnto = 5.50

   imp = mnto*igv

   totalfac = mnto+imp

  elif cn=="f":

   mnto = 4.00

   imp = mnto*igv

   totalfac = mnto+imp

   # Mostrar resultados
 print("|        BOLETA DE VENTAS      |")

 print("| | Subtotal           : ",mnto)

 print("| | Igv                : ",imp)

 print("| | Total a pagar      : ",totalfac)

 print("                                ")

 print("| |    Gracias por tu compra   |")
    
 print("================================")

 print("                                ")

 print("                                ")

 print("                                ")





 if op=="d": break

 time.sleep(20)