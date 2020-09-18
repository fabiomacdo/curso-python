resp = 'S'
soma = 0
count = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / count
print('Você digitou {} números e a média foi {:.2f}.'.format(count, media))
print('O maior entre os números digitados é o {} e o menor {}.'.format(maior, menor))