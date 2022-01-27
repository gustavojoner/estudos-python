n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >=6:
    print ('Sua nota foi boa!')
else:
    print ('Sua nota foi ruim!')