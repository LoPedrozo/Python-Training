soma = 0
for i in range(1,7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        soma = soma + num

    else:
        print('Número ímpar, não será somado.')
print(f'A soma dos números pares é {soma}.')
print('Fim do programa!')


