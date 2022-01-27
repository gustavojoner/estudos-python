lista = []
c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'A lista em decrescente é {lista}')
print(f'{len(lista)} números foram digitados.')
if 5 in lista:
    print('5 está na lista.')
else:
    print('5 não está na lista.')