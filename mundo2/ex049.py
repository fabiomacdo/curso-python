n = int(input('Digite um número: '))
print('A sua tabuada é: ')
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (n * c)))
