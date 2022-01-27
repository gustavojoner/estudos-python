lista = []
par = []
impar = []
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Continuar: [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'Os números digitados foram {lista}.')
print(f'Os números pares são {par}.')
print(f'Os números ímpares são {impar}.')
