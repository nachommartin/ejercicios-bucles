year = int (input ("Introduce el año"))
if year > 0:
    if year % 400 == 0:
            print ("es bisiesto")
    if year % 4 == 0: 
        if year % 100 == 0: 
             year = ("no es bisiesto")
        else:
            year = ("es bisiesto")
            print (year)
    else:
        print ("no es bisiesto")
else: 
    print ("Error")