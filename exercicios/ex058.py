from random import randint
print('Adivinhe o número em que estou pensando, entre 0 e 10')
computador = randint(0, 10)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um valor: '))
    tentativas += 1
    if computador == jogador:
        acertou = True
        print('Parabéns, você acertou em {} tentativas, pensei no número {}.'.format(tentativas, computador))
    elif computador > jogador:
        print('Errou, é mais, tente outra vez')
    else:
        print('Errou, é menos, tente outra vez')
