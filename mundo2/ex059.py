num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('''O que você deseja fazer com esses números? 
           [ 1 ] SOMAR
           [ 2 ] MULTIPLICAR
           [ 3 ] MAIOR
           [ 4 ] NOVOS NÚMEROS
           [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Escolha a opção: '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('o resultado de {} x {} é {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        print('Informe os números novamente.')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do Programa. Volte sempre!')
