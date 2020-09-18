peso = float(input('Qual é o seu peso (em kg)? '))
altura = float(input('Qual é a sua altura (em m)? '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif 25 > imc >= 18.5:
    print('Você está DENTRO do peso ideal.')
elif 30 > imc >= 25:
    print('Você está com SOBREPESO.')
elif 40 > imc >= 30:
    print('Você está com OBESIDADE.')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')