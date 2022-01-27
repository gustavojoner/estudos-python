from time import sleep
from random import randint
lista = []
cont = jogos = 0
n = int(input('Quantos jogos quer que eu sorteie? '))
print('Sorteando os números, aguarde...')
sleep(1)
for c in range(0, n):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    lista.sort()
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
    jogos += 1
    sleep(1)
    if jogos == n:
        break
print('Boa sorte =)')
