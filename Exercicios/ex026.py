frase = input('Digite uma frase: ').strip()
print(f'A letra "A" aparece {frase.lower().count('a')} vezes na frase')
print(f'A letra "A" aparece pela primeiea vez na frase na posição {frase.lower().find('a') + 1}')
print(f'A letra "A" aparece pela ultima vez na frase na posição {frase.lower().rfind('a') + 1}')

