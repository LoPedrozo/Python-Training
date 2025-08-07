cores = {
    'verde':'\033[32m'
}
salario = float(input('Digite o salário: R$ '))
if salario > 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print(f'O novo salário é {cores['verde']}$ {novo:.2f}{cores['verde']}')

