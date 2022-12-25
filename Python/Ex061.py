#Exercício 061 - Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while

#Exercício 51 - feito com a estrutura for
"""p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = p1 + (10 - 1) * r
print('Os 10 primeiros termos da Progressão Aritmética são:')

for c in range(p1, décimo + r, r):
    PA = p1 + (c - 1) * r
    print('{}'.format(c), end = ' → ')
print('FIM')"""

#Resolução do Professor - feito com a estrutura while
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
