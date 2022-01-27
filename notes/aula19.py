dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo']='Masc' #adicionando elemento ao dicionario
print(dados['sexo'])
del dados['idade'] #remover elemento

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Luccas'}
print(filme.values()) #valores
print(filme.keys()) #chaves
print(filme.items()) #valores+chaves
for k, v in filme.items():
    print(f'O {k} é {v}')

#podemos ter dicionarios dentro de listas e tuplas

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #cria copia do elemento do dicionario
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
