sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo inválido. Por favor, Digite novamente seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

