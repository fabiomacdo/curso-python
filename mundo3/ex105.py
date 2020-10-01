def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: dicionário com as notas do aluno.
    :param sit: (opcional) indica se deve ou não adicionar a situação.
    :return: o dicionário com as informações da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(4.5, 5.5, 7, 2.5, sit=True)
print(resp)
help(notas)
