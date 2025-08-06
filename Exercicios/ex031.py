distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <=200:
    preco = distancia * 0.50
    print(f'O valor da sua passagem é R$ {preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O valor da sua passagem é R$ {preco:.2f}')
print('--- FIM ---')

