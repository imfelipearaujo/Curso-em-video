#Aula 11 - Cores no Terminal
#ANSI - escape sequence
#Código ANSI começa com \

#começar uma cor no python: \033[CORAQUIm
#Estilo, texto, background: \033[0;33;44m

#Códigos para estilo:
#0 = sem estilo nenhum (zero ou nada
#1 = coloca o texto em negrito
#4 = sublinhado (underline_
#7 = inverter as configurações (negativo)

#Códigos para cor do texto
#30 = branco
#31 = vermelho
#32 = verde
#33 = amarelo
#34 = azul
#35 = magenta
#36 = ciano
#37 = cinza (cor padrão)

#Códigos para background
#40 = branco
#41 = vermelho
#42 = verde
#43 = amarelo
#44 = azul
#45 = magenta
#46 = ciano
#47 = cinza (cor padrão)

print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')

nome = 'Felipe'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))