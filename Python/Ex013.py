#Exercício 013 - Reajuste salarial
print('Exercício 013 - Faça um algoritmo que'
      ' leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')

salario = float(input('Qual é o salário do funcionário? R$'))
novo = (salario * 15 / 100) + salario
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}!'.format(salario, novo))