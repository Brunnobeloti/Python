from math import sin, tan, cos, radians

angulo = float(input('Digite seu Ângulo: '))

seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seu angulo em um triangulo trigonométrico, pode ser representado por um SENO de {:.2f}'.format(seno))
print('Seu angulo em um triangulo trigonométrico, pode ser representado por um COSENO de {:.2f}'.format(coseno))
print('Seu angulo em um triangulo trigonométrico, pode ser representado por uma TANGENTE de {:.2f}'.format(tangente))