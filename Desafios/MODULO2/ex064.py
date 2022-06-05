n = cont = acumulador = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    cont += 1
    acumulador += n
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} valores, e a soma entre eles é: {}'.format(cont, acumulador))