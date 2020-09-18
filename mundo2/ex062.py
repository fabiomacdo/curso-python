primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('FIM. Progressão finalizada com {} termos mostrados.'.format(total))
