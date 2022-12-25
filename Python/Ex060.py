#Exercício 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120

#Forma 1 - importando biblioteca
"""from math import factorial
num = int(input('Digite um número para\ncalcular seu Fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num, f))
"""
#Forma 2 - usando o while
"""n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))"""

#Forma 3 (desafio) - usando o for
