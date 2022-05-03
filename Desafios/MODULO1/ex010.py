real = float(input('Quantos reais você tem? R$'))
dolar = real / 4.92
euro = real / 5.43
print('Com R${:.2f} você consegue comprar US${:.2f} e £U${:.2f}'.format(real, dolar, euro))