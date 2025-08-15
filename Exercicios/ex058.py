import random
numero = random.randint(1,10)
tentativa = int(input('Tente adivinhar o número que estou pensando entre 1 e 10: '))
erros = 0
while tentativa != numero:
    if tentativa ==  numero:
        print('Você acertou!')
    else:
        erros += 1
        print('Você errou!')
        if tentativa < numero:
            print('O número é maior que o que você tentou.')
        else:
            print('O número é menor que o que você tentou.')
        tentativa = int(input('Tente novamente: '))
print(f'Você acertou! O número era {numero}. Você tentou {erros} vezes.')
if erros == 0:
    print('Você é um gênio!')
print('Fim do Programa!')

