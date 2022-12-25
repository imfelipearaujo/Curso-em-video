#Exercício 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = (casa / (anos * 12))

print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R${:.2f}.'.format(prestacao))
if prestacao <= salario * (30 /100):
    print('\033[1;97;92mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[1;97;41mEmpréstimo NEGADO!\033[m')
