num = contador = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
print('Fim do programa!')
