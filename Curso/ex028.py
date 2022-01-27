from random import randint
from time import sleep
print ('-=-' *11)
numero = int(input('Digite um número entre 0 e 5: '))
numeros = randint(0, 5)
print ('PROCESSANDO...')
sleep(2)
if numeros == numero:
    print ('Parabéns, o número era {}.'.format(numeros))
else:
    print ('Não foi dessa vez! Pensei no número {}.'.format(numeros))
