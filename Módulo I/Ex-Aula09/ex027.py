#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana 
#último = Souza 

nome=str(input('Digite seu nome completo: ')).strip()
nome=nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))#Se não colocar o '-1' o 'len' vai contar como 1 o indice 0 e não dara resultado 

#O [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.
#Portanto, podemos resolver da seguinte forma:
#nome = input('Qual o seu nome completo? ')
#m = nome.split()
#print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')