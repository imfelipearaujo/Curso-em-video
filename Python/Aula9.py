#Aula 9 - Manipulando texto

#Fatiar textos
frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2]) #pula de 2 em 2
print(frase[1::2]) #pula de 2 em 2 mas não sabe o final
print(frase[::2]) #pula de 2 em 2 mas não sabe o início e final
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged.""")
print ('-'*20)
print(' ')


#Análise de uma String
print ('-'*20)
print('Análise de uma String:')
print('Len - ',len(frase))  #Função len (length) = qual é o comprimento da frase
print('Count o - ',frase.count('o',0,13)) #Função count('o') = conta quantos 'o' (minúsculo) existe em determinado texto
print('Find deo - ',frase.find('deo')) #Encontra a posição do texto procurado
print('Find python - ',frase.lower().find('python')) #Transforma todo o texto em mínusculo e procura por python
print('Find Android - ',frase.find('Android')) #Quando retornar -1, significa que o texto procurado não existe
print ('Possuí na frase? - ','Curso' in frase)
print ('-'*20)
print(' ')


#Transformação de uma String
print ('-'*20)
print('Transformação de uma string:')
print('Replace - ',frase.replace('Python', 'Android')) #Troca a palavra Python por Android
print('Upper - ',frase.upper()) #Tudo em maiúsculo
print('Lower - ',frase.lower()) #Tudo em minúsculo
print('Capitalize - ',frase.capitalize()) #transforma a primeira letra em maiúscula
print('Title - ',frase.title()) #Transforma a inicial de cada frase em maiúscula
print('Strip - ',frase.strip()) #Remove os espaços excedentes do início e final da frase
print('Lstrip - ',frase.lstrip()) #Remove os espaços da esquerda
print('Rstrip - ',frase.rstrip()) #Remove os espaços da direita

print ('-'*20)
print(' ')

#Divisão de uma String
print ('-'*20)
print('Divisão de uma String:')
print('Split - ',frase.split()) #Divide a frase onde têm espaços


print ('-'*20)
print(' ')

#Junção de uma String
print ('-'*20)
print('Junção de uma String:')
frase = frase.split()
print('-'.join(frase))
