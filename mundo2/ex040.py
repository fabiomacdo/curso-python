n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é {}'.format(n1, n2, media))
if media < 5.0:
    print('Portanto, o aluno está REPROVADO!')
elif 7.0 > media >= 5.0:
    print('Portanto, o aluno está de RECUPERAÇÃO!')
elif media >= 7.0:
    print('Portanto, o aluno está APROVADO!')