print ("1. Cambio de euros a dolares")
print ("2. Cambio de dolares a euros")
print ("3. Cambio de euros a libras")
print ("4. Cambio de libras a euros")
print ("5. Cambio de libras a dolares")
print ("6. Cambio de dolares a libras")
print ("7. Salir")
num = int (input ("Elige una opcion"))
while num != 7:
    if num == 1:
        cantidad= int (input ("Di cantidad"))
        change= cantidad*1.17
        print ("El cambio es", change, "dolares")
    elif num == 2:
        cantidad= int (input ("Di cantidad"))
        change= cantidad*0.86
        print ("El cambio es", change, "euros")
    elif num == 3:
        cantidad= int (input ("Di cantidad"))
        change= cantidad*0.90
        print ("El cambio es", change, "libras")
    elif num == 4:
        cantidad= int (input ("Di cantidad"))
        change= cantidad*1.11
        print ("El cambio es", change, "euros")
    elif num == 5:
        cantidad= int (input ("Di cantidad"))
        change= cantidad*1.29
        print ("El cambio es", change, "dolares")
    elif num == 6:
        cantidad= int (input ("Di cantidad"))
        change= cantidad*0.77
        print ("El cambio es", change, "libras")
    else:
        print ("Opcion equivocada")
    num = int (input ("Elige una opcion"))