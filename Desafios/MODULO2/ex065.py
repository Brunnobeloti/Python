pergunta = 'S'
cont = 0
acumulador = 0
#while pergunta in 'Ss':
while pergunta == 'S':
    num = int(input('Digite um valor: '))
    cont += 1
    acumulador += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    pergunta = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]

media = acumulador / cont
print('Você digitou {} numeros, e a média foi {}'.format(cont, media))
print('O maior valor doi {} e o menor foi {}'.format(maior, menor))
