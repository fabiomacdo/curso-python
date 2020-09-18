soma = 0
num = 0
count = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        count += 1
print('Acabou. Foram digitados {} números e a soma entre eles é {}'.format(count, soma))
