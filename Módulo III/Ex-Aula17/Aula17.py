#Listas são mutáves, então podemos alterar seus valores, diferente de tuplas.
#Sendo assim em uma lista podemos adicionar valores, remover valores, alterar valores, etc.
print('\n')
print(41*'=')
print('Exemplo de substituição em uma "lista":')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picolé' #Alterando o valor do índice 3
print(lanche)
print(41*'=')
print('\n')

print(41*'=')
print('Exemplo de inserção em uma "lista":')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche.append('cookie') #Adicionando um valor ao final da lista
print(lanche)
print(41*'=')
print('\n')

print(41*'=')
print('Exemplo de inserção em uma posição específca em uma "lista":')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche.insert(0, 'hot-dog') #Adicionando um valor em uma posição específica
print(lanche)
print(41*'=')
print('\n')

#Metodos de remoção de valores de uma lista
#DEL: Remove um valor em uma posição específica
print(41*'=')
print('Método "del" para excluir valor em uma lista:')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
del lanche[3] #Excluindo um valor em uma posição específica
print(lanche)
print(41*'=')
print('\n')
#POP: Remove o último valor da lista
print(41*'=')
print('Método "pop" para excluir valor em uma lista:')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche.pop(2) #Excluindo um valor em uma posição específica
print(lanche)
lanche.pop() #Excluindo o último valor da lista
print(lanche)
print(41*'=')
print('\n')
#REMOVE: Remove um valor específico da lista e reposiciona os valores
print(41*'=')
print('Método "remove" para excluir valor em uma lista:')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche.remove('pizza') #Excluindo um valor específico
print(lanche)
print(41*'=')
print('\n')

#Criando listas 
#RANGE: Cria uma lista com valores de 0 a n-1
print(41*'=')
print('Criando listas com range:')
valores = list(range(4, 11)) #Cria uma lista com valores de 4 a 10  
print(valores)
print(41*'=')   
print('\n')
#Ordem de valores
print(41*'=')
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
print('Ordenando valores:')
valores.sort() #Ordena os valores
print(valores)
print('Ordenando valores de forma reversa:')
valores.sort(reverse=True) #Ordena os valores de forma reversa
print(valores)
print('Quantidade de valores:')
print(f'Essa lista tem {len(valores)} elementos')
print(41*'=')
print('\n')
