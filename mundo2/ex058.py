from random import randint
computador = randint(0, 10) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número ente 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
count = 1
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente novamente.')
    else:
        print('Menos... Tente novamente.')
    count += 1
    jogador = int(input('Em que número eu pensei? '))
print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER!')
print('O NÚMERO QUE PENSEI FOI REALMENTE O {}!'.format(computador))
print('VOCÊ PRECISOU DE {} CHANCES PARA ACERTAR.'.format(count))
