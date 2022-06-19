cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 
        'quinze', 'dezeseis', 'dezesete', 'dezoito', 
        'dezenove', 'vinte')



while True:
    num = int(input('Que numero quer escrito por extenso entre 0 e 20? '))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end=' ')
print(f'O numero {num} escrito por extenso fica: {cont[num]}')
pergunta = str(input('Quer continuar? [S/N] ')).upper.s
    if pergunta == 'SN':
        