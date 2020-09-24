numeros = [[], []]
valor = 0
for n in range(1, 8):
    valor = int(input(f'{n}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')
