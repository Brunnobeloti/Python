times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 
         'Internacional', 'Fluminense', 'Botafogo', 'Santos',
         'São Paulo', 'Bragantino', 'Avaí', 'Atlético-GO', 
         'Ceará SC', 'Flamengo', 'Coritiba', 'América-MG', 
         'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')

print('-=-'*20)
print(f'Os times do Brasileirão 2022 são: {times}')
print('-=-'*20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-=-'*20)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('-=-'*20)
print(f'O Santos está na {times.index("Santos")+1}ª posição')