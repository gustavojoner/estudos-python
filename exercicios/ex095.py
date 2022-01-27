time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols fez na {c+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('Erro, digite novamente.')
    if r in 'N':
        break
print('-'*55)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<20}', end=' ')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<20}', end=' ')
    print()
print('-'*55)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para Fim]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro, digite novamente.')
    else:
        print(f'Levantamento do Jogador {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' -> No jogo {i} fez {g} gols')
    print('-' * 55)
print('Encerrado')
