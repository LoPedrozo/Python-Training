num = int(input('Digite um número: '))
total = 0
for i in range(1, num +1):
    if num % i == 0:
        print('\33[33m', end='')
        total += 1
    else:
        print('\33[31m', end='')
    print(i, end=' ')
print(f'\n\33[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO é PRIMO!')
print('Fim do programa!')


