lista = []
cont = 0
while True:
    lista.append(int(input('Adicione um numero á lista: ')))
    cont += 1
    r = str(input('Deseja adicionar mais um numero? [S/N]'))
    if r in 'Nn':
        break
print(lista)
print(f'Foram digitados {cont} valores!')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')
if '5' in lista:
    print('O valor 5 está na lista! ')
else:
    print('O valor 5 não está na lista! ')
