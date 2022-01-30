# definir funcao
def lin():
    print('---------------------')


lin()
print('--------JONER--------')
lin()

# definir funcao com parametro
def mensagem(msg):
    print('---------------------')
    print(msg)
    print('---------------------')


mensagem('-------GUSTAVO-------')

# deixar duas linhas em branco abaixo da funcao para nao sublinhar e dar liberdade ao comando
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(7, 4)
soma(23, 51)

# podemos mudar a ordem dos valores da definicao
soma(a=4, b=5)
soma(b=4, a=5)

# empacotamento (quantidade indefinida de parametros) - cria tupla
def contador(*num):
    print(num)

contador(2, 1, 7)
contador(8, 4)
contador(1, 5, 6, 8, 2, 3)

def contador2(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('fim')


contador2(1, 2, 3)
contador2(5, 2, 6, 7, 9, 0)

def contador3(*num):
    tamanho = len(num)
    print(f'Os valores são {num}, ao todo {tamanho} números.')


contador3(2, 4, 6, 1)

# listas
valores = [2, 3, 5, 8]
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(valores)


dobra(valores)

# desempacotar

def somando(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


somando(3, 5, 6, 2)

