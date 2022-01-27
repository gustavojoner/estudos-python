print('=$= Conversão de R$ para US$, levando em consideração o câmbio 3,27 =$=')
n = float(input('Qual quantia você deseja converter? R$ '))
d = n / 3.27
print('R$ {:.2f} são US$ {:.2f}'.format(n, d))
