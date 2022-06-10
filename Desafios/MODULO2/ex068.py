from random import randint

print('-'*30)
print('Jogo do PAR ou IMPAR!')
print('-'*30)

while True:
    jogador = int(input('Escolha um numero: '))
    computador = randint(0,10)
    soma = computador + jogador
    print(f'Você escolheu {jogador} e o computador {computador}, a soma é {soma}')
    