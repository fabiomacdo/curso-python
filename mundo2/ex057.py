sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('Opção inválida. Tente novamente!')
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso. Obrigado!'.format(sexo))
