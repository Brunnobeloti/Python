peso = float(input('Qual seu peso atual? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))

imc = peso / (altura ** 2)

print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
elif imc >= 40:
    print('Obesidade móbida!')