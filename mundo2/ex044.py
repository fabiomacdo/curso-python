print('{:=^40}'.format(' LOJAS MACÊDO '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista em dinhero/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Informe a opção: '))
if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco * 1.20
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))
