s = 0
count = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        count += 1
print('Você informou {} números pares e a soma entre eles é {}'.format(count, s))