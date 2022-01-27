from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    resultado = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Você quer Par ou Ímpar? [P/I] ')).strip().upper()
    if escolha in 'Pp':
        if resultado % 2 == 0:
            vitorias += 1
            print(f'Você venceu, escolhi {computador} e você {jogador}, deu Par.')
        else:
            print(f'Você perdeu, escolheu {jogador} e eu {computador}, então deu {jogador + computador}, Ímpar.')
            print(f'Teve {vitorias} vitórias consecutivas.')
            break
    if escolha in 'Ii':
        if resultado % 2 != 0:
            vitorias += 1
            print(f'Você venceu, escolhi {computador} e você {jogador}, deu Ímpar.')
            print('Vamos jogar outra vez.')
        else:
            print(f'Você perdeu, escolheu {jogador} e eu {computador}, então deu {jogador + computador}, Par.')
            print(f'Teve {vitorias} vitórias consecutivas.')
            break
