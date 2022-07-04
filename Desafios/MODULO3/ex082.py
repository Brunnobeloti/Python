from numpy import append


valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Adicione um valor: ')))
    resp = str(input('Deseja adicionar outro valor? '))
    if resp in 'Nn':
        break

for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('='*40)
print(f'Os valores digitados são: {valores}')
print(f'Os valoers pares digitados, são: {pares}')
print(f'Os valores impares digitados são: {impares}')