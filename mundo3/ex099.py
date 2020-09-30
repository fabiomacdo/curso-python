from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} números.')
    print(f'O maior número entre todos os informados é {maior} ')


maior(5, 8, 3, 9, 2)
maior(3, 6)
maior(4, 8, 1)
maior(1)
maior()

