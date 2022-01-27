s = float(input('Informe o salário para calcular o aumento: '))
print ('O valor do no atual do salário é de R$ {:.2f} '.format(s))
if s > 1250:
    print ('O novo salário será de R$ {}'.format((s*10/100)+s))
else:
    print ('O novo salário será de R$ {}'.format((s*15/100)+s))
