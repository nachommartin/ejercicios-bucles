base = int(input("Dime un numero"))
potencia = int(input("Dime otro"))
resultado = 1.0
cont = 1
if potencia < 0:
    fin = -potencia
else: 
    fin = potencia
while (cont <= fin):
    resultado *= base
    cont+=1
if base == 0 and potencia < 0:
    print ("Error")
else: 
    if potencia < 0:
        resultado= 1/resultado
    print ("Resultado de elevar la potencia es", resultado)