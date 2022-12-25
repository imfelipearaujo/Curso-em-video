#Exercício 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Escreva seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculo é', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome[:nome.find(' ')], nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], nome.find(' ')))
