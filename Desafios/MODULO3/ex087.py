matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = soma_pares = 0


for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

soma_valores = matriz[0][2] + matriz[1][2] + matriz[2][2]

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
            cont += 1

print('-'*50)
print(f'A soma dos valores da terceira coluna é: {soma_valores}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print(f'Foram digitados {cont} valores PARES')
print(f'A soma dos valores PARES digitados é :{soma_pares}')
