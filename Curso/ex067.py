while True:
    n = int(input('Insira um valor: '))
    if n < 0:
        print('Até mais.')
        break
    for t in range (1, 11):
        print(f'{t} x {n} = {t*n}')
