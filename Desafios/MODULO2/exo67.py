cont = 0

while True:
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    while True:
        
        cont += 1
        mult = cont * num
        print(f'{num} x {cont:2} = {mult:2}')
        if cont >= 10:
            cont = 0
            break


#while True:
#    num = int(input('Digite um numero: '))
#    if num < 0:
#        break
#    for c in range(1,11):
#        print(f'{num} x {c:2} = {num*c:2}')
        