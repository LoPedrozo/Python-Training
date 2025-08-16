import random
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    op = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    computador = random.randint(0,10)
    soma = jogador + computador
    resultado = 'P' if soma % 2 == 0 else 'I'
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total = {soma}', end=' ')
    print('PAR' if resultado == 'P' else 'ÍMPAR')

    if op == resultado:
        print('Você venceu!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'\nGAME OVER! Você venceu {vitorias} vezes')
