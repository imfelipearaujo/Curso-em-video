#Exercício 012 - Calculando Descontos
print('Exercício 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

preco = float(input('Qual é o preço do produto? R$'))
desc = 0.05
novo = preco - (preco * 0.05)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, novo))