pessoa = list()
dados = list()
pesomax = pesomin = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(dados) == 0:
        pesomax = pesomin = pessoa[1]
    else:
        if pesomax < pessoa[1]:
            pesomax = pessoa[1]
        if pesomin > pessoa[1]:
            pesomin = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    ver = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while ver not in 'SN':
        ver = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ver == 'N':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(dados)} pessoas.')
print(f'O maior peso foi de {pesomax}kg. Peso de ', end='')
for c in dados:
    if c[1] == pesomax:
        print(f'[{c[0]}] ', end='')
print()
print(f'O menor peso foi de {pesomin}kg. Peso de ', end='')
for c in dados:
    if c[1] == pesomin:
        print(f'[{c[0]}] ', end='')
