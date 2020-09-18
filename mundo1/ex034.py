salario = float(input('Informe o seu salário atual: '))
if salario <= 1250:
    aumento = salario + salario * 0.15
else:
    aumento = salario + salario * 0.10
print('O seu novo salário será de R${:.2f}!'.format(aumento))