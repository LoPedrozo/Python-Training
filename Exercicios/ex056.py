nome_mais_velho = ''
idade_mais_velho = 0
quant_mulheres_menor_20 = 0
soma_idades = 0

for i in range (1,5):
    print(f'------ {i}ª Pessoa ---')
    nome = input('Digite o nome: ').strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').strip().upper()

    soma_idades += idade

    if sexo == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

    if sexo == 'F':
        if idade < 20:
            quant_mulheres_menor_20 += 1

    media_idades = soma_idades / 4

print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}.')
print(f'A média de idade do grupo é {media_idades:.1f} anos.')
print(f'O número de mulheres com menos de 20 anos é {quant_mulheres_menor_20}.')
print('--- FIM ---')
