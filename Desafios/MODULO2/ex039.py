from datetime import date
atual = date.today().year

an = int(input('Ano do seu nascimento: '))

sexo = int(input('''Digite:
[1] Se for Homem: 
[2] Se for Mulher: '''))

idade = atual - an

print('-=-' * 20 )

print('Quem nasceu em {} tem {} anos em {}.'.format(an, idade, atual))

if sexo == 2:
    print('Você é mulher, portanto seu alistamento não é Obrigatório!! ')

elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE! ')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento! '.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print('Você já devia ter se alistado há {} anos! '.format(saldo))

print('-=-' * 20 )