tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
          'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude',
          'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-='*15)
print('Lista de Times do Brasileirão')
print('-='*15)
print(f'Os 4 primeiros colocados foram: {tabela[:4]}')
print(f'Os 4 últimos colocados foram: {tabela[-4:]}')
print(f'Times em Ordem Alfabética: {sorted(tabela)}')
print(f'O time Chapecoense ficou na {tabela.index("Chapecoense")+1}ª posição.')