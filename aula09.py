from itertools import count

frase = 'Lorenzo Garcia Pedrozo'
print(len(frase))
print(frase.count('o'))
print(frase.find('e', 5,22))
print(frase.replace('Pedrozo', 'Pirolli'))
frase = frase.replace('Lorenzo', 'Arthur')
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.split())
print('-'.join(frase))
