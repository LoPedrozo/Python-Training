primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('PAUSA')
mais_termos = int(input('Quantos termos a mais você quer mostrar? '))
while mais_termos > 0:
    for i in range(mais_termos):
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos a mais você quer mostrar? '))
print(f'Foram mostrados {contador - 1} termos no total.')
print('FIM')



