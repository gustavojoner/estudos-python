from math import hypot
b = float(input('Insira o cateto oposto= '))
c = float(input('Insira o cateto adjacente= '))
a = hypot(b, c)
print('A hipotenusa é {:.2f}'.format(a))