from math import sin, cos, tan, radians
num = float(input('Informe o valor do ângulo: '))
seno = sin(radians(num))
cosseno = cos(radians(num))
tgt = tan(radians(num))
print('O seno de {} é {:.2f}'.format(num, seno))
print('O cosseno de {} é {:.2f}'.format(num, cosseno))
print('A tangente de {} é {:.2f}'.format(num, tgt))