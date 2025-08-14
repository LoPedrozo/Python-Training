maiorpeso = 0
menorpeso = 0
for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso lido foi {maiorpeso}kg.')
print(f'O menor peso lido foi {menorpeso}kg.')

