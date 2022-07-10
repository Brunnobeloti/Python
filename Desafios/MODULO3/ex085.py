lista = [[], []]
valor = 0
for c in range(1,8):
    valor = (int(input(f'Digite o {c}° numero: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-'*50)
print(f'Os valores impares digitados foram: {lista[1]}')
print(f'Os valores pares digitados foram: {lista[0]}')