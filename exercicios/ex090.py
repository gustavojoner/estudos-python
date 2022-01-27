nome = str(input('Nome do Aluno: '))
media = float(input(f'Média de {nome}: '))
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
aluno = {'Nome': nome, 'Média': media, 'Situação': situacao}
for c, v in aluno.items():
    print(f'{c} é igual a: {v}')
