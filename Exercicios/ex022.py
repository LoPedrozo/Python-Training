from os.path import split

nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print(f'o seu nome ao todo tem {len(nome) - nome.count(' ')} letras')
print(f'o seu primeiro nome tem {len(nome.split()[0])} letras')

