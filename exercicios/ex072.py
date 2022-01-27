n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
     'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    v = int(input('Digite um valor de 0 até 20: '))
    if v >= 0 and v <= 20:
        print(f'Você digitou o número {n[v]}.')
        break
    else:
        print('Valor inválido, tente novamente.')
