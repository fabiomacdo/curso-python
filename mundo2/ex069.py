contidade = 0
conthomem = 0
contmulher = 0
while True:
    print('========== CADASTRO DE PESSOA ==========')
    idade = int(input('Qual a idade da pessoa? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('========== FIM DO PROGRAMA ==========')
print(f'Foram cadastradas {contidade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {conthomem} homens.')
print(f'Foram cadastradas {contmulher} mulheres com menos de 20 anos.')
