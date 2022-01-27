from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
ranking = dict()
for j in range(1, 5):
    dado = randint(1, 6)
    print(f'O Jogador {j} tirou: {dado} ')
    sleep(1)
    jogos[j] = dado

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('O Ranking foi: ')
for j, d in enumerate(ranking):
    print(f'{j+1}º Lugar - Jogador {d[0]} tirou: {d[1]}')
    sleep(1)
