n = int(input('Digite um número: '))
tabuada = (n * i for i in range(1, 11))
print(f'Esta é a tabuada do {n}: \n {list(tabuada)}')