valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi o {max(valores)} e está nas posições ', end='')
for i, c in enumerate(valores):
    if c == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi o {min(valores)} e está nas posições ', end='')
for i, c in enumerate(valores):
    if c == menor:
        print(f'{i}...', end='')
