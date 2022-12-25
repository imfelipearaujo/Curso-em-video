#Exercício 031 - Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200 km e R$ 0,45 para viagens mais longas

viagem = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar a sua viagem de {}Km.'.format(viagem))
if viagem <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.45))


#opção 2
preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))