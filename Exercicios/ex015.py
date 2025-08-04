dias = int(input("Quantos dias alugados? "))
km = float("Quantos km rodados? ")
preco_dia = 60.0
preco_km = 0.15
total = (dias * preco_dia) + (km * preco_km)
print(f"O total a pagar é: R${total:.2f}")