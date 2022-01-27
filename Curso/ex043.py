p = float(input('Peso em Kg (ex: 85.2): '))
a = float(input('Altura em metros (ex: 1.75): '))
imc = p/a**2
if imc < 18.5:
    print('Seu IMC é {:.2f} Kg/m², você está ABAIXO do seu peso ideal.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} Kg/m², você está no seu peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} Kg/m², você está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} Kg/m², você está OBESO.'.format(imc))
else:
    print('Seu IMC é {:.2f} Kg/m², você está com OBESIDADE MORBIDA.'.format(imc))
