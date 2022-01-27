n = str(input('Digite seu nome: ')).title()
s = str(input('Sexo [M/F]: ')).upper().strip()
while s not in 'MF':
        print('Dado Inválido')
        s = str(input('Sexo [M/F]: ')).upper()
if s == 'M':
    print('Seu nome é {} e seu sexo é Masculino.'.format(n))
else:
    print('Seu nome é {n} e seu sexo é Feminino.'.format(n))
