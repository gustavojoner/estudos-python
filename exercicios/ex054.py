from datetime import date
p = 0
y = date.today().year
for c in range (1, 8):
    n = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    if y - n >= 21:
        p += 1
print('{} São maiores de 21 anos e {} são menores de idade.'.format(p, 7-p))
