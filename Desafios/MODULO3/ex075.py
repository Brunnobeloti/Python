numeros = (int(input('Digite um numero: ')), 
            int(input('Digite outro numero: ')), 
            int(input('Digite mais um numero: ')), 
            int(input('Digite um ultimo numero: ')))

print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3)+1}ª posição.')
else:
    print('Não apareceu o numero 3.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')