listagem = ('Notebook', 2300,
            'Mochila', 90,
            'Teclado', 50,
            'Mouse', 25,
            'CPU', 800,
            'Headphone', 120,
            'Webcam', 60,
            'Impressora', 900,
            'Nobreak', 300)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-'*40)
