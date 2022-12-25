#Exercício 010 - Conversor de Moedas
print('Exercício 010 - Crie um programa que leia quanto dinheiro uma pessoa'
      ' tem na carteira e mostre quantos dólares ela pode comprar.')

real = float(input('Quanto dinheiro você tem na carteira? R$:'))
dolar = 4.80
calc = real / dolar
print('Com R${} você pode comprar US${:.2f}, com a cotação do dólar a {:.2f}!'.format(real, calc, dolar))