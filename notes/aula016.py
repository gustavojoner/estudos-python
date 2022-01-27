#TUPLAS SAO IMUTAVEIS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#PARA CADA 'C' EM 'LANCHE' - NAO PRECISA DE POSICAO
'''
for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi pra caramba!')
'''
#COM CONTAGEM E LEN (TAMANHO, NUMERO DE ELEMENTOS) - CASO PRECISE POSICAO
'''
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Vou comer pra caramba!')
'''
#COM ENUMERACAO - CASO PRECISE POSICAO
'''
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print('Comi tanto...')
'''
#SORTED - MOSTRAR EM ORDEM
'''
print(sorted(lanche))
print(lanche)
'''
#COUNT = Numero de vezes que aparece. INDEX = posicao
'''
a = (2, 5, 8)
b = ( 5, 4, 3, 2)
c = a + b
print(c.count(5)) #QUANTAS VEZES APARECE '5'
print(c.index(8)) #Posicao do '8'
'''
#COMANDO DEL APAGA VARIAVEL DA MEMORIA
'''
del(lanche)
'''
