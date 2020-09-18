primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
while count <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    count += 1
print('FIM')
