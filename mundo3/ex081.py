valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    verificador = ' '
    while verificador not in 'SN':
        verificador = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if verificador in 'N':
        break
print(f'Você digitou {len(valores)} números.')
valores.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
