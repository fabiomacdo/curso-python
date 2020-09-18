total = []
while True:
    total.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    verificador = ' '
    while verificador not in 'SN':
        verificador = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if verificador in 'N':
        break

pares = []
impares = []
for c in total:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('-=' * 30)
print(f'A lista completa é: {total}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
