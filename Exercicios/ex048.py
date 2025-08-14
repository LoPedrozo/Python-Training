soma = 0
contator = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contator = contator + 1
        soma = soma + i
print(f'A soma de todos os {contator} valores solicitados é {soma}.')

