num = int (input ("Dime un numero"))
acum= 0
cont= 0
peque= num
mayor= num
while num != 0:
    acum = acum + num
    cont = cont + 1
    media = acum / cont
    if peque > num:  
        peque = num
    else: 
        mayor = num
    num = (input ("Dime un numero"))
print ("La media es", media)
print ("El menor es", peque)
print ("El mayor es", mayor)