n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média final é {media:.1f}')
if media >= 6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')
print('Tenha um bom dia!')
print('--- FIM ---')
