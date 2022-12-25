'''Exercício 054 - Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''
from datetime import date
Atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = int(Atual - nasc)
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))
