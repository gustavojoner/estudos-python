from time import sleep

def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    for valor in num:
        print(f'{valor} ', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
           if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores, o maior é {maior}')
maior(2, 5, 7, 3, 0)
maior(1, 3)
maior(6)
maior()