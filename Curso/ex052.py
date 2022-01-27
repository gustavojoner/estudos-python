n = int(input('Digite um número para saber se ele é Primo: '))
cont = 0
for c in range (1, n+1):
    if n % c == 0:
        print('\033[34m', end=(' '))
        cont += 1
    else:
        print('\033[31m', end=(' '))
    print('{}\033[m'.format(c), end=(' '))
if cont == 2:
    print('\n O Número {} foi divisível apenas 2 vezes, por isso ele é Primo.'.format(n))
else:
    print('\n O Número {} foi divisível {} vezes, por isso ele NÃO é Primo.'.format(n, cont))
