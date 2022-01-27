somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper()
    somaidade += idade
    if c == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher += 1
mediaidade = somaidade/4
print('A média de idade do grupo é de {:.0f} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('{} mulheres tem menos de 20 anos.'.format(totmulher))
