print('-'*30)
print('{:^30}'.format('BANCO BBS'))
print('-'*30)

saque = int(input('Quanto você quer sacar? R$ '))
total = saque
ced = 50
totced = 0

while True:
    if total >= ced:
        ced -= 50
        totced += 1
    else: 
        if totced > 0:
            print(f'Você receberá {totced} notas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if totced == 0:
            break
