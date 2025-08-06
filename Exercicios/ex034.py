salario = float(input('Digite o salário: R$ '))
if salario > 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print(f'O novo salário é R$ {novo:.2f}')

