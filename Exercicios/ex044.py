preco = float(input('Digite o preço da compra: R$ '))
dinheiro = preco - (preco * 0.10)
cartao = preco - (preco * 0.05)
parcelado2x = preco / 2
parcelado_mais_vezes = preco + (preco * 0.20)
print('''Escolha a forma de pagamento:
[ 1 ] Dinheiro/Cheque
[ 2 ] Cartão
[ 3 ] Parcelado em 2x
[ 4 ] Parcelado em 3x ou mais''')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'Você escolheu pagar a vista em dinheiro ou cheque, Você terá um desconto de 10% e o total será R$ {dinheiro:.2f}.')
elif opcao == 2:
    print(f'Você escolheu pagar a vista no cartão, Você terá um desconto de 5% e o total será R$ {cartao:.2f}.')
elif opcao == 3:
    print(f'Você escolheu pagar parcelado em 2x, o valor da parcela será de R$ {parcelado2x:.2f}.')
elif opcao == 4:
    quantas_parcelas = int(input('Quantas parcelas? '))
    parcela = preco / quantas_parcelas
    if quantas_parcelas < 3:
        print('Você deve escolher a opção 3 para parcelar em 2x.')
    else:
        print(f'Você escolheu pagar parcelado em {quantas_parcelas}x, o valor da parcela será de R$ {parcela:.2f} com juros de 20%, totalizando R$ {parcelado_mais_vezes:.2f}.')
else:
    print('Opção inválida. Tente novamente.')
print('--- FIM ---')
