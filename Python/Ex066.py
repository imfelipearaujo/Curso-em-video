#Exercício 066 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
#quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
#e qual foi a soma entre eles (desconsiderando o flag).

#Minha resposta
"""n = s = c = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma entre entres foi de {s}.')"""

#Reposta do professor
soma = cont = 0
while True != 999:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')