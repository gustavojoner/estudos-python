# tratamento de erros

try: # tente isso, se não
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro: # excecao - falha - nome para erros que nao sao no codigo
    print(f'Problema encontrado: {erro}.')
# except (ValueError, TypeError): - para mais de uma excecao com mesma acao deve por em ()
    #print(f'O erro encontrado foi {erro.__cause__)
# except KeyboardInterrupt: - forma de por excecoes
else:
    print(f'O resultado foi {r}.')
finally: # sempre sera executado este comando
    print('Volte sempre, muito obrigado!')
