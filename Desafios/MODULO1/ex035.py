print('-=-'*20)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas a cima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos a cima NÂO PODEM formar um triângul!')
