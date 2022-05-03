from tokenize import triple_quoted


n = float(input('Digite seu numero: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro do seu numero é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(d, t, r))