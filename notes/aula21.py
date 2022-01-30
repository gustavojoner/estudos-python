'''
primeiramente ajuda interativa, abrir console e digitar funcao 'help()',
nela posso consultar as demais funcionalidades da linguagem python,
por exemplo: print, len, input, etc.
apos as consultas, para encerrar, digitar comando 'quit'

outras formas de consultar, é atraves de 'print(funcao.__doc__)' ou 'help(print)'
'''

# utilizacao de docstrings, 3x aspas duplas para criar um help para nossa funcao
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')


help(contador)

# parametros opcionais
def somar(a=0, b=0, c=0): # nao necessario incluir o valor na funcao
    s = a + b + c
    print(f'A soma vale {s}.')


somar(2, 5, 4) # a = 2, b = 5, c = 4
somar(3, 9) # a = 3, b = 9, nao necessita do 3rd parametro, equivale a zero

# retorno
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s # o retorno sera s, a seguir


r1 = soma(2, 3, 5)
r2 = soma(5, 4)
r3 = soma(7)
print(f'Meus calculos deram {r1}, {r2} e {3}.')
