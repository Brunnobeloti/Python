from random import randint

print('Vou pensar em um numero de 0 a 10, Tente adivinhar!')

computador = randint(0,10)

contador = 0

acertou = False

while not acertou:
    jogador = int(input('Faça a sua escolha: '))
    contador += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('''Parabéns, você conseguiu!
Você precisou de {} tentativas!'''.format(contador))