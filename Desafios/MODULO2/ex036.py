# Valor da cara - Salario do comprador - anos para serem pagos
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salario do comprador? R$ '))
anos = float(input('Em quantos anos deseja pagar? '))

prestação = casa / (anos * 12)

minimo = salario*0.30


if prestação <= minimo:
    print('-=-'*20)
    print('Emprestimo APORVADO!')
    print('O valor da sua prestação será R$ de {:.2f}'.format(prestação))
    print('-=-'*20)

elif prestação > minimo:
    print('-=-'*20)
    print('Emprestimo REJEITADO!')
    print('Prestação maior que 30% do salário')
    print('-=-'*20)