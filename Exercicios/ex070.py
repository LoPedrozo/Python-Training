totalcompra = 0
produtos_acimademil = 0
menorpreco = 0
nome_produto_maisbarato = ''
primeiro = True
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o Preço do Produto: R$'))

    totalcompra += preço


    if preço > 1000:
        produtos_acimademil += 1

    if primeiro or preço < menorpreco:
        menorpreco = preço
        nome_produto_maisbarato = nome
        primeiro = False

    op = str(input('Deseja continuar? [S/N]')).strip().upper()
    if op == 'N':
        break


print(f'\nO total gasto com a compra foi de R${totalcompra:.2f}')
print(f'A quantidade de produtos que custaram acima de R$1000 foi {produtos_acimademil}')
print(f'O produto mais barato foi {nome_produto_maisbarato} que custou R${menorpreco}')
