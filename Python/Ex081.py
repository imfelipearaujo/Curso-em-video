#Exercício 081 - Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.
lista = []
resp = 'S'
while resp == 'S':
    n = int(input('Digite um número: '))
    lista.append(n)
    print(lista)
    if 5 in n:
        print('O valor 5 faz parte da lista!')
    else:
        print('O valor 5 não faz parte da lista!')
    resp = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
print('Final do programa')
lista.sort(reverse=True)
print(f'A sua lista foi: {lista}')
#print(f'A sua lista foi: {sorted(lista, reverse=True)}')
print(f'e você digitou {len(lista)} valores.')
if cinco > 0:
    print(f'O número 5 foi digitado {cinco} vezes.')
