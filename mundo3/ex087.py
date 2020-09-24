matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somaterceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}]x[{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somaterceira += matriz[l][c]

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif maior < matriz[1][c]:
        maior = matriz[1][c]

print('-='*30)
print(f'A soma de todos os valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maior}.')

