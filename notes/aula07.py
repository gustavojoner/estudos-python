#LISTA [ ], onde pode ser adicionado e removido itens
lanche = ['Pizza', 'Cookie', 'Hamburguer', 'Suco']
lanche.append('Chocolate') #adiciona item no fim
lanche.insert(0, 'Banana') #adiciona item na posição indicada
del lanche[2] #remove item do numero indicado
lanche.pop(1) #remove ultimo item ou indicado
lanche.remove('Suco') #remove item pelo nome (apenas uma vez)/ if 'Suco' in lanche: (para remover varios ou nenhum)
print(lanche)

valores = [1, 5, 6, 8, 2, 4, 9]
valores.sort() #deixa em ordem
print(valores)
valores.sort(reverse=True) #ordem ao contrario
print(valores)
print(len(valores))

a = [2, 6, 7, 2]
b = a #cria uma ligação, tudo feito em um afeta o outro
b = a[:] #cria uma copia, as alteracoes nao se afetam

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

numeros = list() #cria uma lista
for cont in range(0, 5): #para cada elemento no range de 0 a 5 (que ainda esta vazio)
    numeros.append(int(input('Digite um valor: '))) #add um valor escolhido no fim
print(numeros)

num = [2, 5, 9, 4]
num [2] = 3 #substitui o valor indicado
print(num)
