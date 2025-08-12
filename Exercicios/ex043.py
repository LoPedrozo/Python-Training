peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
print('--- FIM ---')
