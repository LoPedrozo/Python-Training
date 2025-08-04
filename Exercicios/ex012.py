preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 0.05
precofinal = preco - desconto
print(f'O preço do produto com 5% de desconto é: R${precofinal:.2f}')
