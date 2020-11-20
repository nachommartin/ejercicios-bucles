ejex= input ("Di la coordenada 1")
ejey= input ("Di la coordenada 2")
cuadrante= 0
if ejex >0 and ejey >0:
    cuadrante = "Primer cuadrante"
elif ejex  <0 and ejey >0:
    cuadrante = "Segundo cuadrante"
elif ejex <0 and ejey <0:
    cuadrante = "Tercer cuadrante"
elif ejex >0 and ejey <0:
    cuadrante = "Cuarto cuadrante"
elif ejex ==0 and ejey ==0:
    cuadrante = "centro"
print ("Estas en el", cuadrante)