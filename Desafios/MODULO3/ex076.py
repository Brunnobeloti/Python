listagem = ('Caderno', 22.40,
            'Lápis', 1.20,
            'Caneta', 1.50,
            'Mochila', 170,
            'Borracha', 0.70,
            'Corretivo', 2.15,
            'Régua', 3,
            'Estojo', 5.50,
            'Livro', 23,)

print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)