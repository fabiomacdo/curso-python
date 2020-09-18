n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('{} é MAIOR'.format(n1))
elif n1 < n2:
    print('{} é MAIOR'.format(n2))
else:
    print('Não existe valor maior, os dois são IGUAIS!')
