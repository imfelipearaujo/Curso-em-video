#Exercício 073 - Crie um Tupla preenchida com os 20 primeiro colocados da Tabela do Campeonato Brasileiro de Futebol
# na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiro colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time do São Paulo.

#Minha resposta
"""classificação = ('Corinthians', 'Santos', 'Avaí', 'América-MG', 'Bragantino', 'Palmeiras', 'Atlético-MG', 'São Paulo',
                 'Botafogo', 'Flamengo', 'Internacional', 'Coritiba', 'Cuiabá', 'Athletico-PR', 'Fluminense',
                 'Goiás', 'Ceará SC', 'Juventude', 'Atlético-GO', 'Fortaleza')
print('Os 5 primeiro colocados são:')
for pos, time in enumerate(classificação[0:5]):
    print(f'Na {pos + 1}ª posição está o time: {time}.')
print('=-' * 20)
print(' ')

print('Os 4 últimos colocados são:')
for pos, time in enumerate(classificação[-4:]):
    print(f'Na {pos + 1}ª posição está o time: {time}.')
print('=-' * 20)
print(' ')

print('Times em ordem alfabética: ')
print(sorted(classificação))
print('=-' * 20)
print(' ')

print('O São Paulo está na posição: ', end='')
print((classificação.index('São Paulo')))"""

#Resposta do professor
times = ('Corinthians', 'Santos', 'Avaí', 'América-MG',
         'Bragantino', 'Palmeiras', 'Atlético-MG', 'São Paulo',
         'Botafogo', 'Flamengo', 'Internacional', 'Coritiba',
         'Cuiabá', 'Athletico-PR', 'Fluminense', 'Goiás',
         'Ceará SC', 'Juventude', 'Atlético-GO', 'Fortaleza')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição.')