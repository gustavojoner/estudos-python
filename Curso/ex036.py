vc = float(input('Qual o valor do imóvel? '))
s = float(input('Qual seu salário? '))
t = float(input('Pretende pagar em quantos anos? '))
vp = (vc/(t*12))
if vp > (s*30/100):
    print('O valor da parcela (R${:.2f}) não pode ser superior a 30% do seu salário (R${:.2f})!'.format(vp, s))
    print('Financiamento não aprovado!')
else:
    print('Parabéns, seu financiamento foi aprovado!')
    print('Você pagará {} vezes de R${:.2f} num imóvel de valor R${:.2f}!'.format(t*12, vp, vc))
