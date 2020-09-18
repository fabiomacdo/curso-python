vel = float(input('Qual sua velocidade atual em km/h? '))
if vel > 80.0:
    print('VOCÊ FOI MULTADO POR EXCESSO DE VELOCIDADE!')
    multa = (vel - 80.0) * 7
    print('O VALOR DA MULTA É DE R${:.2f}'.format(multa))
print('DIRIJA COM SEGURANÇA E TENHA UMA BOA VIAGEM!')