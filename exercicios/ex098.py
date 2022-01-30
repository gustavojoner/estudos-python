from time import sleep

def contador(i, f, p):
    if p < 0: # caso o valor seja negativo
        p *= -1
    if p == 0: #caso o valor seja zero
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            c += p
            sleep(0.5)
        print('Fim.')

    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            c -= p
            sleep(0.5)
        print('Fim.')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pular: '))

contador(i, f, p)
