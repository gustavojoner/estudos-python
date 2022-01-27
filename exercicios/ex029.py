v = float(input('A velocidade lida foi: '))
if v >80:
    print ('Você passou a {} km/h em uma via de limite 80km/h'.format(v))
    print ('Sua multa será de R$ {:.2f}'.format((v-80)*7))
    print ('Dirija com moderação!')
else:
    print ('Obrigado por respeitar o limite de velocidade!')
