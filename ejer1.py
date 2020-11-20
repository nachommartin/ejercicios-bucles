acum=0 #Guardo la suma longitudes
lados= int(input ("Cuantos lados tiene?")) #para saber los lados
while int (lados) < 3:
    print("No es valido")
    lados = int (input("Debe tener tres, prueba otra vez"))
for num in range (1, lados + 1):
    longi = int (input("Que longitud tiene cada lado"))
    while int(longi) <= 0:
        print("La longitud debe ser mas de cero")
        longi = int (input("Prueba otra vez"))
    acum = acum + longi 
peri= acum
print ("El perimetro es", peri)