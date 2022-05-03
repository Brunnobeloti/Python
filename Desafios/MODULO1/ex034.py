salario = float(input('Qual o seu salario: '))

if salario < 2500:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print('O seu salario foi de R${:.2f} para R${:.2f}'.format(salario, aumento))
