n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto {} e a divisão {:.2f}'.format(s, m, d))
print('A divisão inteira é {} e a potência {}'.format(di, e))

print('A soma vale {},\n o produto {}\n e a divisão {:.2f}'.format(s, m, d))
print('A divisão inteira é {}\n e a potência {}'.format(di, e))

print('A soma vale {}, o produto {} e a divisão {:.2f}'.format(s, m, d), end=' >>> ')
print('A divisão inteira é {} e a potência {}'.format(di, e))
