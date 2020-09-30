from time import sleep

def contador(i, f, p):
    print('-=' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Sua vez de personalizar a contagem! ')
ini = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
contador(ini, final, passo)
