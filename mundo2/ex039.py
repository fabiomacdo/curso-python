from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
idade = (date.today().year) - ano
print('Quem nasceu em {} faz {} anos esse ano.'.format(ano, idade))
if idade > 18:
    saldo = idade - 18
    print('Você já passou do tempo de alistamento.')
    print('Você deveria ter se alistado a {} ano(s) atrás, em {}.'.format((saldo), (ano + 18)))
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda vai se alistar.')
    print('O seu ano de alistamento é daqui a {} ano(s), em {}.'.format((saldo), (ano + 18)))
else:
    print('Está na hora de você se alistar!')