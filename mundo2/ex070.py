total = 0
maismil = 0
count = 0
baratopreco = 0
baratonome = ''
print('==========  LOJA SUPER BARATÃO ==========')
while True:
    produto = str(input('Qual o nome do produto? ')).strip()
    preco = float(input('Qual o preço desse produto? R$'))
    total += preco
    if count == 0:
        baratopreco = preco
        baratonome = produto
        count = 1
    if preco > 1000:
        maismil += 1
    if preco < baratopreco:
        baratopreco = preco
        baratonome = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('=======================================')
print('========== FIM DAS COMPRAS ==========')
print(f'O total gasto nas compras foi de R${total:.2f}')
print(f'{maismil} produtos custam mais de R$1000.00')
print(f'O produto mais barato é {baratonome} que custa R${baratopreco:.2f}')
