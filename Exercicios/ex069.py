maiorIdade = 0
homens = 0
Fmenor20 = 0
while True:
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()


    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maiorIdade += 1
    if sexo == 'F':
        if idade < 20:
          Fmenor20 += 1
    op = str(input('Deseja continuar? [S/N]')).strip().upper()
    if op == 'N':
        break

print(f'Você digitou {maiorIdade} pessoas maiores de Idade')
print(f'Você Cadastrou {homens} Homens')
print(f'Você digitou {Fmenor20} mulher com menos de 20 anos')

