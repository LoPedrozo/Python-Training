nome = str(input('Digite um nome: ')).strip().lower()
if nome == 'lorenzo':
    print('Belo Nome!')
elif nome == 'aslam':
    print('Zabour!')
elif nome in ('maria', 'joão', 'pedro'):
    print('Nome comum!')
else:
    print('Nome normal!')

print(f'Prazer {nome.capitalize()}!')
print('--- FIM ---')
