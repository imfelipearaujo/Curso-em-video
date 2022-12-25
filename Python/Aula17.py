#Aula 17 Parte 1 - Listas []
#Teoria
'As listas podem ser mutavéis'
"""lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.append('Cookie') #Com append, é adicionado um novo item no final da lista
#Caso queira colocar entre itens:
lanche.insert(0, 'Cachorro Quente') #Adiciona em qualquer posição
print(lanche)"""

#Apagar itens da lista
#Comando DEL
"""del(lanche[3])
lanche.pop(3) #método POP geralmente é para eliminar o último elemento, mas também pode usar em qualquer item.
lanche.remove('Pizza') #O remove é usado para apagar pelo valor
print(lanche)
lanche.pop() #Usado dessa forma, elimina o último item
if 'Pizza' in lanche:
    lanche.remove('Pizza')
else:
    print('Não tinha pizza no lanche!')
print(lanche)"""

#Criar listas através de ranges
"""valores = list(range(4, 11)) #Usando a função list

#Colocar os valores em ordem:
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() #Ordena todos os valores na ordem crescente
valores.sort(reverse=True) #Ordena todos os valores na ordem decrescente
print(valores)

#Para saber o tamanho da lista:
print(len(valores))"""

#Parte prática da aula
#Listas são mutáveis, exemplo abaixo:
"""num = [2, 5, 9, 1]
num[2] = 3
#num[4] = 7 #Não é possível adicionar valores dessa maneira, precisa fazer:
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2) #Adicionando um número que já existe.
num.remove(2) #Procura a primeira ocorrência
#num.pop() #Elimina o último número da lista
#num.remove(4) #Não existe o 4 na lista, daria erro, mas para isso é só criar um laço (if)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')"""

#mostrando a lista de forma mais bonita
#Para criar uma lista vazia tem duas formas:
# valores = []
# valores = list()
"""valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) #Inserindo valores na lista através do teclado
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')"""
"""a = [2, 3, 4, 7]
b = a #Quando uma lista é igual a outra, o python faz uma ligação entre elas e não uma cópia
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')"""

#Para fazer uma cópia da lista:
a = [2, 3, 4, 7]
b = a[:] #A lista b está recebendo todos os itens de a, nessa caso, fazendo uma cópia.
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')