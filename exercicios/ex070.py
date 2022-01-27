barato = ' '
menorvalor = soma = produtos = cont = 0
while True:
    print('--------CADASTRE UM PRODUTO--------')
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$ '))
    cont += 1
    soma += valor
    if valor > 1000:
        produtos += 1
    if cont == 1 or valor < menorvalor:
        menorvalor = valor
        barato = nome
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()[0]
    if escolha in 'Nn':
        break
print(f'O total da compra foi R${soma}')
print(f'Temos {produtos} produtos que custam mais de R$1000.00')
print(f'O mais barato foi {barato} custando {menorvalor}.')

