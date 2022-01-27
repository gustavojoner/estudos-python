from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor foi {max(numeros)}.')
print(f'O menor valor foi {min(numeros)}.')

'''
while True:
    n = randint(0, 100)
    v1 = n
    menor = n
    maior = n
    n = randint(0, 100)
    v2 = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    n = randint(0, 100)
    v3 = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    n = randint(0, 100)
    v4 = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    n = randint(0, 100)
    v5 = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    break
numeros = (v1, v2, v3, v4, v5)
print(f'Entre os valores: {numeros}. O menor valor é {menor} e o maior valor é {maior}.')
'''