nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é legal.')
elif nome in 'Juliana Ana Cláudia Jéssica':
    print('Que nome bonito e feminino.')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))
