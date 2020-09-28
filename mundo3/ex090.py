aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-=' * 15)
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A sua média é {aluno["média"]}')
print(f'Sua situação é {aluno["situação"]}')
