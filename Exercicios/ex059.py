num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    print('Escolha uma opção:')
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Sair do programa')
    op = int(input('Opção: '))
    if op == 1:
        soma = num1 + num2
        print(f'A soma de {num1} + {num2} é {soma}.')
    elif op == 2:
        mult = num1 * num2
        print(f'A multiplicação de {num1} X {num2} é {mult}.')
    elif op == 3:
        if num1 == num2:
            print('Os números são iguais.')
        else:
            maior = max(num1, num2)
            print(f'O maior número entre {num1} e {num2} é {maior}.')
    elif op == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida! Tente novamente.')
print('Programa encerrado. Até logo!')
