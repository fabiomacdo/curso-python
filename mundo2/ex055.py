maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa, em kg: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso informado foi {:.1f}kg'.format(maior))
print('E o menor peso informado foi {:.1f}kg'.format(menor))
