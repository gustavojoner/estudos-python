from datetime import date
ano = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
i = ano - nasc
if i <= 9:
    print('Sua idade é {} anos no ano atual, você está na categoria MIRIM.'.format(i))
elif i > 9 and i <= 14:
    print('Sua idade é {} anos no ano atual, você está na categoria INFANTIL.'.format(i))
elif i > 14 and i <= 19:
    print('Sua idade é {} anos no ano atual, você está na categoria JUNIOR.'.format(i))
elif i == 20:
    print('Sua idade é 20 anos no ano atual, você está na categoria SÊNIOR.')
else:
    print('Sua idade é {} anos no ano atual, você está na categoria MASTER.'.format(i))
