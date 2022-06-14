print('-'*30)
print('Loja do Joãozinho')


totvalor = caros = 0

while True:
    print('-'*30)
    Nomep = str(input('Digite o nome do produto: '))
    valorp = float(input('Digite o valor do produto: R$ '))
    totvalor += valorp
    if valorp > 1000:
        caros += 1
    pergunta = str(input('Você deseja continuar? [S/N] ')).split()[0].upper()
    if pergunta == 'N':
        break




print('-'*30)

print(f'O valor total da compra foi {totvalor}. ')
print(f'Foram comprados {caros} produtos que custam mais de R$ 1.000,00. ')
print(f'O produto mais barato foi {valorp} custando apenas {valorp}.')
