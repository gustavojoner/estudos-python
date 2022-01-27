lista = ('Aprender', 'Python', 'Programar', 'Back-end', 'Futuro')
for p in lista:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for l in p:
        if l in 'aeiou':
            print(l.upper(), end=' ')