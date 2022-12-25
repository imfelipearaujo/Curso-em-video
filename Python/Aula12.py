#Aula 12 - Condições aninhadas
'Parte teórica'
#carro.siga()
#se carro.esquerda()            if carro.esquerda():
    #carro.siga()
    #carro.direita()
    #carro.siga()
    #carro.direita()
    #carro.esquerda()
    #carro.siga()
    #carro.direita()
    #carro.siga()
#senão se carro.direita()       elif carro.direita()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
#senão                          else:
    #carro.siga()
#carro.pare()

#elif = else + if
#else é opcional

''''Parte prática'
'Condição simples'
nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))

'Condição Composta'
nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))'''

'Estrutura Condicional aninhada'
nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))