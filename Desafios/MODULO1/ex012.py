preco = float(input('O preco do seu produto é: R$'))

desc = preco * 5 / 100

pf = preco - desc

##pf = preco - (preco * 5 / 100)

print('Parabéns, você ganhou um desconto de R${}, seu produto agora custa R${:.2f}'.format(desc, pf))
