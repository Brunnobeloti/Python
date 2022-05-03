nome = str(input('Digite o nome do(a) aluno(a)! '))
n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qua a segunda nota? '))

nf = (n1 + n2) / 2

if nf < 5.0:
    print('{} tirou {:.1f} e {:.1f}, seua média final é {:.1f}! '.format(nome, n1, n2, nf))
    print('REPROVADO!! ;( ')

elif nf <= 6.9:
    print('{} tirou {:.1f} e {:.1f}, seua média final é {:.1f}! '.format(nome, n1, n2, nf))
    print('RECUPERAÇÂO!! ;|')

else:
    print('{} tirou {:.1f} e {:.1f}, seua média final é {:.1f}! '.format(nome, n1, n2, nf))
    print('APROVADO!! ;)')
