from math import factorial

num = int(input('Digite um número para calcular o fatorial: '))
factorial(num)
contador = num
print(f'Calculando o fatorial de {num}!')
while contador > 0:
    print(contador, end='')
    print(' X ' if contador > 1 else ' = ', end='')
    contador -= 1
print(factorial(num))

