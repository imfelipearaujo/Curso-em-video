#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensage:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

v1 = int(input('Escreva um número: '))
v2 = int(input('Escreva outro número: '))

if v1 > v2:
    print('O PRIMEIRO valor é maior.')
elif v2 > v1:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são iguais.')
