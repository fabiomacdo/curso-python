num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Esse valor já existe. Tente um outro diferente!')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
num.sort()
print(f'Você digitou os valores {num}')
