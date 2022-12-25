#Exercício 029 - Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada KM acima do limite.

velocidade = float(input('Qual a velocidade do veículo?'))
multa = (velocidade - 80.0) * 7

if velocidade > 80.0:
    print('\033[1;30;41mMULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m'
          '\nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Boa viagem!')