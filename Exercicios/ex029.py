velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R$ {multa:.2f} por excesso de velocidade!')
else:
    print('Você está dentro do limite de velocidade. Continue dirigindo com segurança!')
print('--- FIM ---')

