from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 se não): '))
if pessoa['ctps'] != 0:
    pessoa['contrato'] = int(input('Ano de contratação: '))
    pessoa ['salario'] = float(input('Salário atual: R$'))
    pessoa['aposentadoria'] = 35 - (date.today().year - pessoa['contrato']) + pessoa['idade']
print(pessoa)

for c, v in pessoa.items():
    print(f'{c} tem valor {v}')
