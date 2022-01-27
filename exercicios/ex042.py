r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('As retas formam um triângulo EQUILÁTERO.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print ('As retas formam um triângulo ESCALENO.')
    else:
        print ('As retas formam um triângulo ISÓCELES.')
else:
    print ('As retas não formam um triângulo.')
