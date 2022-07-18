ficha= {}

nome_do_al = str(input('Nome do aluno: '))
media_do_al = float(input('Média do aluno: '))

ficha['nome'] = nome_do_al
ficha['media'] = media_do_al

if media_do_al < 5:
    ficha['situação'] = 'Reprovado'
elif media_do_al < 7:
    ficha['situação'] = 'de Recuperação'
else:
    ficha['situação'] = 'Aprovado'


print('-'*59)

print(f'- Nome é igual a {ficha["nome"]}')
print(f'- Média é igual a {ficha["media"]}')
print(f'- A situação é igual a {ficha["situação"]}')