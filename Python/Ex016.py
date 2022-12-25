# Exercício 016 - Quebrando um número
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
#Exemplo:Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.

#from math import trunc
#num = float(input('Digite um número: '))
#print('O valor digitado foi de {:.3f} e a sua porção inteira é {}.'. format(num, trunc(num)))

#O de cima e o de baixo funcionam normalmente, oq diferencia uma da outra é que na de cima importei somente
# a função trunc e na debaixo importei a biblioteca toda

'''import math
num = float(input('Digite um número: '))
print('O valor digitado foi de {:.3f} e a sua porção inteira é {}.'. format(num, math.trunc(num)))'''

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
