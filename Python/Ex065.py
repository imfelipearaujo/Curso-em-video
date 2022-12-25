#Exercício 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
#média entre todos os valores e qual foi o maior valor e o menor alor lidos. O programa deve perguntar ao usuário
#se ele quer ou não continuar a digitar valores

#Minha Resposta
"""r = 'S'
c = 0
soma = 0
num = int(input('Digite um valor: '))
while r == 'S':
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r == 'S':
        num = int(input('Digite um valor: '))
        c = c + 1
        soma = soma + num
    else:
        print('A contagem foi de {} e a media {:.2f} '.format(c, soma / c))"""

#Resposta do professor
resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
