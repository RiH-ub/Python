# Calcular el Sueldo a Pagar
# Gratificacion x fiestas en Julio Diciembre equivalen a un sueldo básico 
# Gratificacion por escolaridad en el mes de Febrero equivale a una Remuneración Mínima Vital
# Calcular el monto a pagar por la empresa a Essalud - 9%

# Ingreso de datos
wsBasico = float(input("Ingrese el sueldo basico    "))
wRMV = float(input("Ingrese el RMV       "))
wMes = int(input("Mes del cálculo de planilla      "))

cComFija = 8.5
cComVar = 1.8
cSAFP = 1.2

# Procesamiento
wSBruto = wsBasico
if (wMes == 2) :
  wSBruto = wSBruto + wRMV

if (wMes == 7) :
  wSBruto = wsBasico * 2

if (wMes == 12) :
  wSBruto = wsBasico * 2

cComFija = wSBruto * cComFija / 100
cComVar = wSBruto * cComVar / 100
cSAFP = wSBruto * cSAFP / 100

wSNeto = wSBruto - (cComFija + cComVar + cSAFP)
wAEsSalud = wSBruto *0.09

# Salida
print ("Detalle de pago")
print ("Sueldo Bruto        s/."+ str(wSBruto))
print ("Comisión Fija       s/."+ str(cComFija))
print ("Comision Variable   s/."+ str(cComVar))
print ("Seguro AFP          s/."+ str(cSAFP))
print ("Sueldo a pagar                 s/."+ str(wSNeto))
print ("")
print ("Aporte del empleado ESSalud    s/."+ str(wAEsSalud))