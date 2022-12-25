#Exercício 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
AnoAtual = date.today().year
maioridade = (nascimento + 18)  #ano
idade = (AnoAtual - nascimento)

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, AnoAtual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    ano = AnoAtual + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))

elif idade > 18:
    saldo = idade - 18
    ano = AnoAtual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))
