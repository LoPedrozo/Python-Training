from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc
print(f'A sua idade é {idade} anos.')
if idade <= 9:
    print('A categoria é MIRIM.')
elif idade <= 14:
    print('A categoria é INFANTIL.')
elif idade <= 19:
    print('A categoria é JÚNIOR.')
elif idade <= 25:
    print('A categoria é SÊNIOR.')
else:
    print('A categoria é MASTER.')
print('--- FIM ---')