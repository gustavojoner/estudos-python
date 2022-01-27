ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')
print('-'*26)
while True:
    opc = int(input('Mostrar notas de qual aluno? [999] para encerrar: '))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print('-' * 50)
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        print('-' * 50)