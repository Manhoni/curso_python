preco = float(input('Qual o valor das compras: R$ '))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão débito\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
pagto = int(input('Qual é a opção de pagamento: '))
if 0 < pagto <= 4:
    if pagto == 1:
        total = preco - (preco * 10 / 100)
    elif pagto == 2:
        total = preco - (preco * 5 / 100)
    elif pagto == 3:
        total = preco
        print(f'A compra fica com preço de R${total:.2f} em duas parcelas de R${total/2:.2f}')
    elif pagto == 4:
        total = preco + (preco * 20 / 100)
        parc = int(input('Quantas parcelas: '))
        print(f'A compra fica com preço de R${total:.2f} em {parc} parcelas de R${total/parc:.2f}.')
    print(f'O valor da compra de R${preco:.2f} fica R${total:.2f}.')
else:
    print('Opção de pagamento não listada, reinicie o programa.')
