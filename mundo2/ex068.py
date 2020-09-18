from random import randint
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
count = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    soma = pc + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total: {soma}')
    if (soma % 2 == 0 and escolha == 'P') or (soma % 2 != 0 and escolha == 'I'):
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        count += 1
    else:
        break
print(f'GAME OVER! Você venceu {count} vezes.')

