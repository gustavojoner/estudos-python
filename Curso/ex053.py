t = str(input('Digite a frase para saber se é um Palíndromo: ')).strip()
t1 = t.replace(" ", "").upper()
t2 = t1[::-1]
if t1 == t2:
    print('A frase "{}" é um Palíndromo.'.format(t1))
    print('Seu inverso é "{}".'.format(t2))
else:
    print('A frase "{}" NÃO é um Palíndromo.'.format(t1))
    print('Seu inverso é "{}".'.format(t2))
