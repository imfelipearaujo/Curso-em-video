#Exercício 015 - Aluguel de Carros
print("""Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$199,98 por dia e R$0,90 por Km rodado.""")
print(' ')
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
pago = (dias * 199.98) + (km * 0.90)
print('O total a pagar é de R${:.2f}'.format(pago))

