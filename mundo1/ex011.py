h = float(input('Informe a altura da parede (em metros): '))
l = float(input('Informe a largura da parede (em metros): '))
a = h * l
t = a / 2
print('A área da parede é {:.2f} m²'.format(a))
print('Precisará de {:.2f} litros de tinta para pintar toda a parede'.format(t))