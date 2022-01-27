print('Cálculo para estimar a quantidade de tinta necessária para uma parede.')
h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
t = (h*l) / 2
print('Sua parede tem {} x {} que equivale a uma área de {:.3f}.'.format(h, l, h*l))
print('Você precisará de {:.3f} litro(s) de tinta.'.format(t))
