from datetime import date

ano = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = ano - nasc
print('-=-' * 20 )
print('O atleta tem {} anos'.format(idade))
print('Categoria: ')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

print('-=-' * 20 )