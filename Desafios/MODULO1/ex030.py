num = int(input('Digite um numero qualquer: '))

res = num % 2

if res == 0:
    print('O numero {} é PAR!'.format(num))
else:
    print('O numero {} é IMPAR!'.format(num))