"""print('Listas são mutáveis, ou seja, podem ser alteradas. São definidas por colchetes e vírgulas.')
dados=list()
dados.append('Pedro')
dados.append(25)
print(dados)
print(dados[0]) #Acessando os elementos da lista
print(dados[1]) #Acessando os elementos da lista
print(dados[0:2]) #Fatiamento
dados[0]='Maria' #Alterando o valor de um elemento
print(dados)
dados[1]=30
print(dados)
##############################################################
print('\nCópia de uma lista')
pessoas = list()
pessoas.append(dados[:]) #Cópia de uma lista
print(pessoas)
dados[0]='João' #Alterando o valor de um elemento
dados[1]=19
pessoas.append(dados[:]) #Cópia de uma lista
print(pessoas)
##############################################################
print('\nLista de listas')
pessoas = [['Pedro', 25], ['Maria', 30], ['João', 19]] #Lista de listas
print(pessoas)
print(pessoas[0]) #Acessando os elementos da lista
print(pessoas[0][0]) 
print(pessoas[0][1])
print(pessoas[1])
###############################################################
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.') #Iterando sobre a lista de listas
print('\n')"""
###############################################################
print('Exemplo prático')
galera = list()
dado = list()
totmai = totmen = 0 #Contadores
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Cópia de uma lista
    dado.clear() #Limpa a lista
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1 
print(f'Temos {len(galera)} pessoas cadastradas.')
print(f'Temos {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade.')