s = 0
n = 0
for c in range(0, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        n += 1
print('A soma dos {} números ímpares que são múltiplos de três entre 1 e 500 é {}'.format(n, s))
