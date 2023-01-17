import time

print("Precios de un producto")
precio=float(input("Ingresar precio de producto: "))

if precio<=20:
	print("El precio del producto es barato")
	
elif precio<=50:
    print("El precio del producto es normal")
    
else:
	print("El precio del producto es caro")

time.sleep(10)


