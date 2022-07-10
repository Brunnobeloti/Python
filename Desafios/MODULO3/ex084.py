temp = []
dados = []

while True:
    temp.append(str(input('Nome ')))
    temp.append(float(input('Peso: ')))
    dados.append(temp[:])
    temp.clear()
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
print(dados)