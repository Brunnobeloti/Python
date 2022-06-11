from random import randint

vitorias = 0

print('-'*30)
print('Jogo do PAR ou IMPAR!')


while True:
    print('-'*30)
    jogador = int(input('Escolha um numero: '))
    computador = randint(0,10)
    soma = computador + jogador
    div = soma % 2
    if div == 1:
        res = 'Impar'
    else:
        res = 'Par'
    escolha = str(input('Escolha Impar ou Par: [I/P] ')).split()[0].upper()
    print('-'*30)
    print(f'Você escolheu {jogador} e o computador {computador}, a soma é {soma}, deu {res}')
    if escolha == 'P':
        print('Você ganhou!')
        vitorias += 1
    else:
        break

print(f'Game Over! Você venceu {vitorias} vezes')
print('-'*30)