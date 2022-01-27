a = int(input('Insira o termo: '))
r = int(input('Insira a razão: '))
c = 1
t = 0
m = 10
while m != 0:
    t += m
    while c <= t:
        print('{} '.format(a), end='')
        a += r
        c += 1
    m = int(input('\nQuer ver mais quantos termos? [0] Para encerrar: '))
print('Terminamos mostrando {} termos, até mais :)'.format(t))
