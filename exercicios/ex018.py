from math import radians, sin, cos, tan
a = float(input('Insira um ângulo= '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Para o ângulo {} temos, seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(a, s, c, t))
