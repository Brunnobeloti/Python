from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um numero de 0 a 5, tente adivinhar!')
print('-=-'*20)

jogador = int(input('Em que numero eu pensei? '))

computador = randint(0,5)

print('PENSANDO...')
sleep(3)

if jogador == computador:
    print('Parabéns! Você ganhou!! ;) ')
else:
    print('PERDEU!! Ganhei de você hahah ;) ')
    print('Pensei no numero {} e não no {}!'.format(computador, jogador))

