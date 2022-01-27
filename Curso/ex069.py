adultos = homens = jovens = pessoas = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Inserir mais pessoas? [S/N]')).strip().upper()[0]
    if idade > 18:
        adultos += 1
    if sexo in 'Mm':
        homens += 1
        pessoas += 1
    if sexo in 'Ff':
        pessoas += 1
    if sexo in 'Ff' and idade < 20:
        jovens += 1
    if continuar in 'Nn':
        print(f'Total de {pessoas} pessoas, sendo {adultos} com mais de 18 anos.')
        print(f'Temos {homens} homens e {jovens} mulheres com menos de 20 anos.')
        break
