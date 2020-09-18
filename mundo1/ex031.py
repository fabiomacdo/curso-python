viagem = float(input('Qual a distância da viagem em km? '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('Sua viagem de {} km custará R${:.2f}!'.format(viagem, preco))