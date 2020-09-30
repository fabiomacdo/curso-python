def area(l, c):
    a = l * c
    print(f'A áreca de um terreno {l} x {c} é de {a}m²')


#Programa Principal
print('Controle de Terrenos')
print('-' * 15)
largura = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(largura, comp)
