def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: tente um número inteiro válido.')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: tente um número real válido.')
        else:
            return n


n1 = leiaInt('Valor Inteiro: ')
n2 = leiaFloat('Valor Real: ')
print(f'O número digitado inteiro foi {n1} e real foi {n2}.')
