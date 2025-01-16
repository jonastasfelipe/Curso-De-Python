#Tuplas são imutáveis, ou seja, não podem ser alteradas. São definidas por parênteses e vírgulas.
num = (2, 5, 9, 1)
print(num)
print(num[2])
print('\n')
#Listas são mutáveis, ou seja, podem ser alteradas. São definidas por colchetes e vírgulas.
num = [2, 5, 9, 1]
print(num)
num[2] = 3 #Altera o valor na posição 2
num.append(7) #Adiciona um valor ao final da lista
print(num)
num.sort() #Ordena os valores
print(num)
num.insert(2, 0) #Adiciona um valor na posição 2
print(num)
num.pop() #Remove o último valor da lista
print(num)
num.pop(2) #Remove o valor na posição 2
print(num)
if 4 in num:
    num.remove(4) #Remove o valor 4 da lista
else:
    print('Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos.')
print('\n')

#Começando uma lista vazia
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores: #Para cada valor em valores
    print(f'{v} ', end='')
print('\n')
for c, v in enumerate(valores): #enumerate() retorna o índice e o valor
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('\n')

valores = list() #Cria uma lista vazia
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('\n') 
# Ligaçãos entre listas
a = [2, 3, 4, 7]
b = a #Liga a lista b à lista a
b[2] = 8 #Altera o valor na posição 2 da lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('\n')
#Cópia de listas
a = [2, 3, 4, 7]
b = a[:] #Copia os valores da lista a para a lista b
b[2] = 8 #Altera o valor na posição 2 da lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('\n')