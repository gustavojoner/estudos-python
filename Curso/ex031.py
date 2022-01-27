d = float(input('Distância percorrida: '))
print ('A distância percorrida foi de {} Km.'.format(d))
if d <= 200:
    print ('O valor da passagem será de R$ {}'.format(d*0.5))
else:
    print('O valor da passagem será de R$ {}'.format(d*0.45))
