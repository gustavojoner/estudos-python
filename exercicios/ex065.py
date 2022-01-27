r = 'S'
m = s = c = maior = menor = 0
while r in 'Sn':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
m = s/c
print('Você digitou {} números e a média foi {}, o maior número foi {} e o menor {}.'.format(c, m, maior, menor))
