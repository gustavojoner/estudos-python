jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols fez na {c+1}ª partida? ')))
jogador['gols'] = partidas[:] #copia
jogador['total'] = sum(partidas) #soma
print()
print(jogador)
print()
for c, v in jogador.items():
    print(f'A {c} tem valor {v}')
print()
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
print()
for p, g in enumerate(jogador['gols']):
    print(f' -> Na partida {p+1}, fez {g} gols.')
