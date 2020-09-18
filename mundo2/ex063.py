print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    count += 1
    t1 = t2
    t2 = t3
print(' -> FIM')
print('-'*30)
