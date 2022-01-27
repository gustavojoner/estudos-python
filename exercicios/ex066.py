n = s = c = 0
while n != 999:
    n = int(input('Insira um número ou [999] Parar: '))
    if n != 999:
        c += 1
        s += n
print('A soma entre os {} números digitados deu {}.'.format(c, s))
