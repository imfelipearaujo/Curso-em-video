'''Exercício 053 - Crie um programa que leia uma frase qualquer e diga se ela é um políndromo,
desconsiderando os espaços.'''
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = '' #utilizando o for
inverso = junto[::-1] #utilizando o fatiamento
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')