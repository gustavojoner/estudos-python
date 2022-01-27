frase = str(input('Digite a frase: ')).lower().strip()
print('A frase tem {} letras "a".'.format(frase.count('a')))
print('A primeira letra "a" apareceu na posição {}.'.format(frase.find('a')+1))
print('A última letra "a" apareceu na posição {}.'.format(frase.rfind('a')+1))
