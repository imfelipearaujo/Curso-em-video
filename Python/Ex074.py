#Exercício 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
#Minha resposta
"""from random import randint
cont = menor = maior = 0

while cont != 5:
    tupla = (randint(0, 10))
    if menor == 0:
        menor = tupla
    while tupla < menor:
        menor = tupla
    if maior == 0:
        maior = tupla
    while tupla > maior:
        maior = tupla
    print(tupla, end=' ')
    cont += 1
print(f'\nO maior valor digitado foi {maior}, e o menor foi {menor}.')"""

#Resposta do professor
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')