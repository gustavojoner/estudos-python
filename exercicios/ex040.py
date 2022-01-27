n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('Sua média foi {}, você foi REPROVADO!'.format(m))
elif m > 5 and m < 7:
    print('Sua média foi {}, você está em RECUPERAÇÃO!'.format(m))
else:
    print('Sua média foi {}, você foi APROVADO!'.format(m))
    print('Parabéns!')
