num = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
    else:
        print('Valor duplicado, não adicionado.')
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
num.sort()
print(f'Você digitou os valores {num}')
