
while True:
    num = int(input('Quer ver o valor de qual tabuada? '))

    if num < 0:
     break
        
    for i in range(1,11):
        mult = num * i
        print(f'{num} X {i} = {mult}')

print('Programa encerrado, volte sempre!')