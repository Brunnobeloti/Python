from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

jogador = int(input('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura
Qual é a sua jogada? '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('='*20)
print('Computador escolheu: {}'.format(itens[computador]))
print('Jogador escolheu: {}'.format(itens[jogador]))
print('='*20)

if computador == 0:
    if jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 0:
        print('EMPATE!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Opção inválida! Tente novamente!')

elif computador == 1:
    if jogador == 2:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 0:
        print('COMPUTADOR VENCEU!')
    else:
        print('Opção inválida! Tente novamente!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('Opção inválida! Tente novamente!')
