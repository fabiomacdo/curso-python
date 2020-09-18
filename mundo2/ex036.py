casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto é o seu salário? R$ '))
anos = int(input('Em quantos anos você deseja financiar a casa? '))
prestacao = casa / (anos * 12)
limite = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= limite:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')