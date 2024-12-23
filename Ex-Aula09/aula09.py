#Manipulando Texto

#Fatiamento de string
frase='Curso em Video Python' #Normal
frase2='  Aprenda Python  ' #Com espaços 
frase3=['Curso', 'em', 'Video', 'Python'] #Em uma lista
print(frase[9]) #identifica o indice específico/ O indice começa com 0 que é a letra C
print(frase[9:13]) #Identifíca uma cadeia específica de índices
print(frase[9:21]) #Identifíca uma cadeia específica de índices
print(frase[9:21:2]) #O :2 salta de dois em dois os indices
print(frase[:5]) #É a mesma coisa de 0:5 vai começar do indice 0
print(frase[15:]) #A mesma primiça do exemplo da linha 6 e 8
print(frase[9::3]) #Vai começar do índice 9 até o final pulando 3 indices

#Análise
print(len(frase)) #len vem de length=comprimento e essa função mostra a quantidade de índices
print(frase.count('o')) #Essa função conta quantos (o que estiver entre parenteses)
print(frase.count('o',0,13)) #Faz uma contagem com fatiamento
print(frase.find('deo')) #Vai mostrar o índice que começa esse conjunto de letras
print('Curso'in frase) #Irá mostrar se existe ou não (operador)

#Transformação 
print(frase.replace('Python','Android')) #Vai substituir a frase 'Pynthon' por 'Android'
print(frase.upper()) #Todos os indices com letras maiúsculas (método)
print(frase.lower()) #Todos os índices com letras minúsculas 
print(frase.capitalize()) #Vai deixar apenas a primeira letra da frase em maiúsculo0
print(frase.title()) #Vai transformar a primeira letra de todas as palavras maiúsculas
print(frase2.strip()) #Vai remover os espaços inúteis do começo e do fim da frase
print(frase2.rstrip()) #Vai remover os espaços inúteis do fim da frase (r de right=direita)
print(frase2.lstrip()) #Vai remover os espaços inúteis do começo da frase (l de left)
print(frase.split()) #Vai dividir as palavras, formando uma lista de todas as palavras de uma cadeia de caracteris 

#Junção
print('-'.join(frase3)) #Junta os elementos de frase que estão separadas em uma lista 
