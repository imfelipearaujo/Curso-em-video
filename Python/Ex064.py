#Exercício 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
#foi a soma entre eles (desconsiderando o flag)
#Minha resolução
"""n = int(input('Digite um número: '))
flag = 999
cont = 0
soma = 0
while n != flag:
    n = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + n
print('Finalizamos! Você digitou {} números e a soma entre eles é igual a {}.'.format(cont, soma - flag))"""

#Resolução do professor
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: ')) #flag do lado de fora
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: ')) #flag dentro do while como ultima linha
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
