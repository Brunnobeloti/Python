salario = float(input('O salário do funcionário é de R$'))

aumento = salario + (salario * 15 / 100)

print('O salário do funcionário é {:.2f},com aumento de 15%, passou a ganhar R${:.2f}'.format(salario, aumento))


