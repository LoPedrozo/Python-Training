num = cont = soma = 0
while True:
    num = int(input('Digite um valor: '))

    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')