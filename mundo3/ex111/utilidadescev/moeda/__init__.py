def aumentar(preco=0, taxa=0, format=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param format: se quer ou não a saída formatada.
    :return: o valor reajustado, com ou sem formatação.
    """
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>1.2f}'.replace('.', ',')


def resumo(preco=0, taxaAum=10, taxaRed=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaAum}% de aumento: \t{aumentar(preco, taxaAum, True)}')
    print(f'{taxaRed}% de redução: \t{diminuir(preco, taxaRed, True)}')
    print('-' * 30)
