lista = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'desesseis', 'desessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número digitado foi o {lista[num]}.')
        cont = str(input('Você quer continuar? [S/N]:  ')).strip().upper()[0]
        while cont not in 'SN':
            cont = str(input('Opção inválida. Você quer continuar? [S/N]:  ')).strip().upper()[0]
        if cont == 'N':
            break
    else:
        print('Tente novamente. ', end='')
print('Fim do programa.')
