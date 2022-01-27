ma = 0
me = 0
for c in range (1,6):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('O maior peso é {}Kg e o menor peso é {}Kg.'.format(ma, me))
