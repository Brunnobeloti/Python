distancia = float(input('Qual a dstancia da sua viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O valor de sa viagem será de R${:.2f}'.format(valor))