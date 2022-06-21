from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), )

print('Numeros sorteados: ', end=' ')

for n in numeros:
    print(n, end=' ')

print(f'\nO menor numero sorteado foi: {min(numeros)}')
print(f'O maior numero sorteado foi: {max(numeros)}')