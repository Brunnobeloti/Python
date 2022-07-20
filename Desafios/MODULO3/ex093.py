dados = {}
gols = []

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
    
print('-=' *30)
print(dados)
print('-=' *30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' *30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'  => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols')