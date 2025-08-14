import datetime
atual = datetime.date.today()
tmaior = 0
tmenor = 0
for pessoas in range(1,8):
    nas = int(input(f'Digite o ano de nascimento da {pessoas}ª pessoa: '))
    idade = atual.year - nas
    if idade >= 18:
        tmaior += 1
    else:
        tmenor += 1
print(f'Temos {tmaior} pessoas maiores de idade e {tmenor} menores de idade.')



