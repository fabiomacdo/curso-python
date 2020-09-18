from math import hypot
ca = float(input('Informe o valor do cateto adjacente: '))
co = float(input('Informe o valor do cateto oposto: '))
h = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(h))