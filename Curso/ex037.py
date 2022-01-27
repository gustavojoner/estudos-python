n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
e = int(input('Sua opção: '))
if e == 1:
    print('{} convertido para Binário é {}'.format(n, bin(n)[2:]))
elif e == 2:
    print('{} convertido para Octal é {}'.format(n, oct(n)[2:]))
elif e == 3:
    print('{} convertido para Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção Inválida')
