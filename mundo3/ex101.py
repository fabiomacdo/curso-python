def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if 18 > idade >= 16 or idade >= 65:
        return f'Com {idade} anos o voto é OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos o voto é NEGADO'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'


ano = int(input('Informe o seu ano de nascimento: '))
print(voto(ano))
