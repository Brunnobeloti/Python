for x in range(1,5):
    print('---- {}ª PESSOA ----'.format(x))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))



print('A média de idade do grupo é de {} anos'.format(idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade, nome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(sexo))
