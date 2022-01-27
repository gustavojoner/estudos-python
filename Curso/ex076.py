lista = ('Pão', 4.50, 'Leite', 4.99, 'Arroz', 7.90, 'Feijão', 6.59, 'Açúcar', 4.29)
cont = 0
print(f'{"LISTA MERCADO":-^40}')
while cont < len(lista):
    print(f'{lista[cont]:.<30} R$ {lista[cont+1]:>5.2f}')
    cont += 2
print('-'*40)