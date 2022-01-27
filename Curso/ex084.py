temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')).capitalize().strip())
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()
    r = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'Número de pessoas cadastradas: {len(principal)}')
print(f'O maior peso foi de {maior}, peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}, peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end='')
