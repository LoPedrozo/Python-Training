idade = int(input('Digite sua idade: '))
if idade < 18:
    anos = 18 - idade
    print(f'Você ainda vai se alistar. Faltam {anos} anos para o alistamento.')
    ano = anos + 2025
    print(f'Seu alistamento será em {ano}.')
elif idade == 18:
    print(f'Sua idade é {idade} anos. Você deve se alistar IMEDIATAMENTE!')
else:
    anos = idade - 18
    print(f'Você já deveria ter se alistado há {anos} anos.')
    ano = 2025 - anos
    print(f'Seu alistamento foi em {ano}.')
print('--- FIM ---')
