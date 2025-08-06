import random
numero = random.randint(0, 5)
chute = int(input('Tente adivinhar o número que estou pensando entre 0 e 5: '))
if chute == numero:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! Eu estava pensando no número {numero}.')



