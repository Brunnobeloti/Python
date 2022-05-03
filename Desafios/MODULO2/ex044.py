print('=' * 10, 'LOJAS BRUNNO`S','=' * 10)

preco = float(input('Valor a ser pago: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista no DINHEIRO/PIX.
[2] À vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão.''')

opcao = int(input('Qual a sua opção? '))

if opcao == 1:
    total = preco - (preco * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    parcelas = preco / 2
    print('Sua compra será parcelada em {}x de R${:.2f} SEM JUROS'.format(2, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco))
elif opcao == 4:
    total = preco + (preco * 0.20)
    tparcelas = int(input('Quantas parcelas?'))
    parcelas = total / tparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(tparcelas, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    print('Opção de pagamento INVÁLIDA!!')
    

