termo = int(input('Digite um termo da PA: '))
razao = int(input('Digite a razão da PA: '))
décimo = termo + (10 - 1) * razao
for i in range(termo,décimo + razao, razao):
    print(i, end=' ')
print('Fim do programa!')