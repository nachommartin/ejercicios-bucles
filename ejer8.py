gollocal = 0
golvisi = 0
jornada = input("Cuántos partidos se han jugado")
for i in range (1,int(jornada) + 1):
    gollocal = int (input("Di goles locales"))
    golvisi = int (input ("Di goles visitantes"))
    while gollocal < 0 or golvisi < 0:
        print("Resultado no válido")
        gollocal = int (input("Di goles locales"))
        golvisi = int (input ("Di goles visitantes"))
    if gollocal > golvisi:
        mensaje = "1"
    elif gollocal < golvisi:
        mensaje = "2"
    else:
        mensaje = "X"
    print(mensaje)