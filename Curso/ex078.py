lista = []
maior = 0
menor = 0
for l in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if l == 0:
        maior = menor = lista[l]
    else:
        if lista[l] > maior:
            maior = lista[l]
        if lista[l] < menor:
            menor = lista[l]
print(f'A lista é {lista}')
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end='')
print(f'\nO menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end='')
