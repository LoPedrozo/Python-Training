
op = 'S'
soma = contador = media = maiornum = menornum =  0
while op == 'S':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maiornum = menornum = num
    else:
        if num > maiornum:
            maiornum = num
        if num < menornum:
            menornum = num

    op = input('Quer continuar? [S/N] ').strip().upper()[0]
    media = soma / contador
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
print(f'A média dos valores digitados é {media:.2f}.')
print(f'O maior valor foi {maiornum} e o menor valor foi {menornum}.')



