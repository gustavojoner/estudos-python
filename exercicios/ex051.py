print('Progressão Aritimética')
a = int(input('Digite um termo: '))
r = int(input('Digite a razão: '))
for c in range (1, 11 ):
    print(a + (c-1) * r, end=(' '))
