'''Exercício 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('=' * 30)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 30)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = p1 + (10 - 1) * r
print('Os 10 primeiros termos da Progressão Aritmética são:')

for c in range(p1, décimo + r, r):
    PA = p1 + (c - 1) * r
    print('{}'.format(c), end = ' → ')
print('ACABOU')

