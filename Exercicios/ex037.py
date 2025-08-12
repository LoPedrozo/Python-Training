num = int(input('Digite um número: '))
binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('Escolha uma opção (1/2/3): '))
if opcao == 1:
    print(f'O número {num} em binário é {binario}.')
elif opcao == 2:
    print(f'O número {num} em octal é {octal}.')
elif opcao == 3:
    print(f'O número {num} em hexadecimal é {hexadecimal}.')
else:
    print('Opção inválida. Tente novamente.')
print('--- FIM ---')
