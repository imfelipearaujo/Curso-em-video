#Exercício 070 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$ 1000
#C) Qual é o nome do produto mais barato
#Minha resposta
"""resp = 'S'
somapreços = maiormil = 0
barato = 1000000
nomebarato = ''
while resp == 'S':
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: '))
    somapreços += preço
    if preço > 1000:
        maiormil += 1
    if preço < barato:
        if preço > barato:
            nomebarato = ''
        elif preço < barato:
            nomebarato = produto
        barato = preço
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('FIM DO PROGRAMA!')
print(f'O total da compra foi \33[34mR${somapreços:.2f}\33[m.')
if maiormil == 1:
    palavra = 'produto que custou'
else:
    palavra = 'produtos que custaram'
print(f'Temos \33[34m{maiormil}\33[m {palavra} mais de \33[34mR$1000\33[m.')
print(f'O produto mais barato foi \33[34m{produto}\33[m e custou \33[34mR${barato:.2f}\33[m.')"""

#Resposta do professor
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 100:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
