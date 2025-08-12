valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = valorcasa / (anos * 12)
minimo = salario * 0.30
print(f'Para pagar uma casa de R$ {valorcasa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo aprovado!')
else:
    print('O empréstimo foi negado!')
print('--- FIM ---')