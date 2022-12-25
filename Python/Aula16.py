#Aula 16 - Variáveis Compostas (Tuplas)
#Teoria
#Três tipos de variáveis compostas:
#1ª tuplas - As tuplas são imutáveis! ()
#2ª listas []
#3ª dicionários{}

"""As tuplas são IMUTÁVEIS, ou seja, não é possível mudar os valores da variável, somente se parar o programa
trocar manualmente, e iniciar novamente"""
#Parte prática da aula
'Toda tupla começa com parenteses, ou sem nada'
# Tuplas são imutáveis
"""lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # ou lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(sorted(lanche)) #ordenar

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#Para saber a posição do item na tupla
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(lanche[1])
print(lanche[1:3])
print(lanche[-2])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])"""

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)
print(len(c))       #Comprimento de C
print(c.count(5))   #Quantas vezes aparece o número 5
print(c.index(8)    #Em que posição está o 1º Nº 8?

pessoa = ('Felipe', 28, 'M')
del(pessoa[1]) #A Tupla é imutável, por tanto, dará erro
del(pessoa) #É possível deletar toda a tupla, mas não um item dentro da tupla

#Exercícios dessa aula:
#Exercício 072
#Exercício 073
#Exercício 074
#Exercício 075
#Exercício 076
#Exercício 077
