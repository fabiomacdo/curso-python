num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('Você digitou os números: ', end='')
for c in num:
    print(c, end=' ')
print(f'\nO valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro 3 digitado está na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
