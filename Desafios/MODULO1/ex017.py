'''from math import sqrt


ca = float(input('Digite o valor do Cateto A: '))
co = float(input('digite o valor do Cateto O: '))

h = ca**2 + co**2       ####  (h = ca**2 + co**2) ** 1/2 

hyp = sqrt(h)

print('Se seu CA é {} e seu é {}, sua hypotenusa será: {:.1f}'.format(ca, co, hyp))'''

from math import hypot

ca = float(input('Digite o valor do Cateto A: '))
co = float(input('digite o valor do Cateto O: '))

hyp = hypot(ca, co)

print('Se seu CA é {} e seu é {}, sua hypotenusa será: {:.1f}'.format(ca, co, hyp))
