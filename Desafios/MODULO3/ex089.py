ficha = []

while True:
    nome = str(input('Nome: '))  #Recebe o Nome dao aluno
    nota1 = float(input('Nota 1: '))  #Recebe a primeira nota do aluno  
    nota2 = float(input('Nota 2: '))   #Recebe a segunda nota do aluno
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    
    pergunta = str(input('Quer continuar? '))
    if pergunta in 'Nn':
        break
print('-=' *30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*36)
    opc = int(input('Deseja ver as notas de qual aluno? ( 999 para interromper!): '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}')

print('<<< VOLTE SEMPRE! >>>')
