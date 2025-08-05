from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
print(f'O ângulo de {ang} tem o seno de {sen:.2f}')
cos = cos(radians(ang))
print(f'O ângulo de {ang} tem o cosseno de {cos:.2f}')
tang = tan(radians(ang))
print(f'O ângulo de {ang} tem a tangente de {tang:.2f}')



