dias = float(input('quantos dias o carro foi alugado?'))
km = float(input('quantos km foram rodados?'))

d = dias * 60
kms = km * 0.15

total = d + kms

## total = (dias * 60) + (km * 0.15)

print('O valor total a pagar é de R${:.2f}'.format(total))
