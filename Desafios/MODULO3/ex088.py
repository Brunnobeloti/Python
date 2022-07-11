from random import randint
from time import sleep

tot = 1
numeros = []
jogos = []

print('-'*30)
print('    JOGA NA MEGA SENA    ')
print('-'*30)

quant = int(input('Quantos jogos quer que eu sorteie? '))

while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont >= 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    tot += 1
print('-=' * 3, 'SORTEANDO', '-=' * 3)

for i, n in enumerate(jogos):
    print(f'JOGO {i+1}: {n}')
    sleep(.5)

print('='*5,'BOA SORTE!', '='*5)
