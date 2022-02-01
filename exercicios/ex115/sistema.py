from ex115.lib.arquivo import *
from ex115.lib.interface import * # tudo
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Cadastro', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Finalizando Sistema.')
        break
    else:
        cabecalho('\033[31mOpção inválida, tente novamente.\033[m')
    sleep(1)
