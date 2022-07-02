numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor já adicionado, tente novamente! ')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você adicionou os valores: {numeros}')