resultado = 0
escolha = 0
while not escolha == 5:
    print('-------------------------------')
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    escolha = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Finalizar
Qual operação deseja realizar: '''))
    if escolha == 1:
        resultado = n1 + n2
        print('A soma é {}.'.format(resultado))
    if escolha == 2:
        resultado = n1 * n2
        print('A multiplicação dá {}.'.format(resultado))
    if escolha == 3:
        if n1 > n2:
            resultado = n1
            print('O maior número é {}.'.format(resultado))
        else:
            resultado = n2
            print('O maior número é {}.'.format(resultado))
    if escolha not in [1,2,3,4,5] and escolha != 4:
        print('Opção Inválida')
else:
    print('-------------------------------')
    print('Até mais.')
