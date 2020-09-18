print('-------------------------------------')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for count in range(1, 11):
        print(f'{n} x {count} = {n*count}')
    print('-------------------------------------')
print('Fim da tabuada. Volte sempre!')
