r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os segmentos não podem formar um triângulo.')
print('--- FIM ---')
