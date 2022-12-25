#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente.

#No final, mostre o conteúdo das três listas geradas

lista1 = []
Par = []
Ímpar = []

while True:
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        lista1.append(n)
        Par.append(n)
    else:
        lista1.append(n)
        Ímpar.append(n)
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Você digitou {lista1}')
print(f'Dentre os números digitados, {Par} são pares e {Ímpar} são ímpares.')
