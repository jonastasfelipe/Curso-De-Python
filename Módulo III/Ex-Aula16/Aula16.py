lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])

for comida in lanche: #Para cada comida em lanche
    print(f'Eu vou comer {comida}')
    
for cont in range(0, len(lanche)): #O len é para contar a quantidade de elementos
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche): #Enumerate é uma função que mostra a posição de cada elemento
    print(f'Eu vou comer {comida} na posição {pos}')
    
print(sorted(lanche)) #Ordena a tupla em ordem alfabética
print(lanche) #A tupla original não muda 

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Concatenação
print(c)
print(c.count(5)) #Conta quantas vezes aparece o número 5 
print(c.index(8)) #Mostra em que posição está o número 8
print(c.index(5, 1)) #Procura o número 5 a partir da posição 1

pessoa = ('Jonatas', 24, 'M', 110)
del(pessoa) #Deleta a tupla
print(pessoa)
