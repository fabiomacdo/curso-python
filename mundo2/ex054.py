from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também {} pessoas menores de idade'.format(menor))
