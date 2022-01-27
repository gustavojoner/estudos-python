n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
if n1 > n2:
    print('{} é maior que {}, então o primeiro número digitado é maior!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}, então o segundo número digitado é maior!'.format(n2, n1))
else:
    print('{} é igual a {}'.format(n1, n2))
