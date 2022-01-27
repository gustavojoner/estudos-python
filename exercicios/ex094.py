galera = list()
pessoa = dict()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, digite novamente.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('Erro, digite novamente.')
    if r in 'N':
        break
media = soma/len(galera)
print()
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade foi de {media:.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('As pessoas com a idade acima da média foram ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' ')
print()
