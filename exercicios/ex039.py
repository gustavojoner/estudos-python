from datetime import date
ano = date.today().year
nasc = int(input('Qual o ano de seu nascimento? '))
if ano - nasc == 18:
    print('Você deverá se alistar no ano atual, pois completará 18 anos em {}.'.format(ano))
elif ano - nasc > 18 :
    print('Você já passou da idade de se alistar, pois terá {} anos em {}.'.format(ano - nasc, ano))
else:
    print('Você deverá se alistar em {} quando completar 18 anos.'.format((nasc + 18)))
