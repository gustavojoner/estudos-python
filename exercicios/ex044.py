valor = float(input('Insira o valor do produto: '))
forma = int(input('''Insira a forma de pagamento
[1] À vista Dinheiro/Cheque
[2] À vista Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão
Sua opção: '''))
if forma == 1:
    print('O valor com o desconto À vista no Dinheiro/cheque será de R${:.2f}'.format(valor-(valor*10/100)))
elif forma == 2:
    print('O valor com o desconto À vista no Cartão será de R${:.2f}'.format(valor-(valor*5/100)))
elif forma == 3:
    print('O valor será de 2 Parcelas de R${:.2f}'.format(valor/2))
elif forma == 4:
    parcelas = float(input('Em quantas vezes deseja fazer o pagamento? '))
    valornovo = valor + (valor*20/100)
    parcela = valor / parcelas
    print('O valor será de R${:.2f}, em {:.0f} parcelas de R${:.2f}'.format(valornovo, parcelas, parcela))
else:
    print('Opção inválida.')
