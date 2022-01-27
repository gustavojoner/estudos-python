from random import choice
j1 = int(input('''Opções:
[1] Pedra
[2] Papel
[3] Tesoura
Sua escolha: '''))
l = [1, 2, 3]
j2 = choice(l)
dic = {1:'Pedra', 2:'Papel', 3:'Tesoura'}
if j1 == j2:
    print('EMPATE, ambos escolhemos {}.'.format(dic[j1]))
elif j1 == 1 and j2 == 2 or j1 == 2 and j2 == 3 or j1 == 3 and j2 == 1:
    print('Você PERDEU, {} perde para {}.'.format(dic[j1], dic[j2]))
else:
    print('Você GANHOU, {} ganha de {}.'.format(dic[j1], dic[j2]))
