n = (int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
     print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
     print('O valor 3 não foi digitado nenhuma vez.')
print('Os valores pares são: ', end='')
for num in n:
     if num % 2 == 0:
          print(num, end=' ')
