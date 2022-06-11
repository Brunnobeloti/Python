homens = mulheres = cont = 0


print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)

while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        cont += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulheres += 1

    print('-'*30)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homens} homem cadastrado. ')
print(f'Temos {mulheres} mulheres com menos de 20 anos. ')
