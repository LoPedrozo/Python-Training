n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'O resultado da soma entre os números digitados é {soma}')
