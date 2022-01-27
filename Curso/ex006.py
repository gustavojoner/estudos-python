n = float(input('Digite um número '))
d = n * 2
t = n * 3
r = n ** (1/2)
cor = {'l':'\033[m', 'a':'\033[33m', 'r':'\033[35m', 'c':'\033[36m'}
print('Seu dobro é {}{}{}, seu triplo é {}{}{} e sua raiz quadrada {}{:.3f}{}.'.format(cor['a'], d, cor['l'], cor['r'], t, cor['l'], cor['c'], r, cor['l']))
