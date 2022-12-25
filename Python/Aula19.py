"""Aula 19 - Dicionários (Variáveis Compostas)
#Parte teórica
Tuplas = ()
Listas = []
Dicionários = {}

dados = ['Pedro', 25]
print(dados[0] = 'Pedro'
print(dados[1] = 25

seria muito melhor, ao invés de chamar de dados[0], chamar de nome
seria muito melhor, ao invés de chamar de dados[1], chamar de idade

Dicionários:
dados = dict() ou  dados = {}

dados = {'nome': 'Pedro', 'idade':, 25}
Não existe mais dados[0] ou dados [1], agora será: dados['nome'] ou dados['idade']
print(dados['nome'] = Pedro
print(dados['idade'] = 25

#Para adicionar elementos em um dicionário:
No caso do dicionário, o append não funciona, eu posso simplesmente criar um novo elemento usando o comando: dados ['sexo']='M'

#Para remover elemntos em um dicionário:
del dados['idade']

#Outro exemplo de dicionário:
filme ={'título':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }
Estes são elementos chaves (keys)
print(filme.values()) #Retorna todos os VALORES

Se eu quiser os títulos, devo usar:
print(filme.keys())

Se eu quiser os títulos e os valores, devo usar:
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

"""
#Parte prática
dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo']='M'
del dados['idade']
print(dados)

filme = {'título':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }
print(filme.values())
print(filme.keys())
print(filme.items())
print('-=' * 30)
for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = [{'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'título': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'título': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[2]['título'])
print('-=' * 30)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append((estado.copy()))
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print('-=' * 30)