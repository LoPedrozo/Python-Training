import random
while True:
    jogador = input('Escolha Pedra, Papel ou Tesoura: ').strip().lower()
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)
    print(f'Você escolheu: {jogador}')
    print(f'O computador escolheu: {computador}')
    if jogador == computador:
        print('Empate!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'papel' and computador == 'pedra') or \
            (jogador == 'tesoura' and computador == 'papel'):
        print('Você ganhou!')
    else:
        print('O computador ganhou!')

    continuar = input('Deseja jogar novamente? (s/n): ').strip().lower()
    if continuar != 's':
        break
    print('Claro! Vamos jogar novamente.')

print('Obrigado por jogar!')
print('--------------------------- FIM ---------------------------')


