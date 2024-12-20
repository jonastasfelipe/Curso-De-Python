#Tipos de formatação
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #Prazer em te conhecer Guilherme           !
print('Prazer em te conhecer {:>20}!'.format(nome)) #Prazer em te conhecer            Guilherme!
print('Prazer em te conhecer {:<20}!'.format(nome)) #Prazer em te conhecer Guilherme           !
print('Prazer em te conhecer {:^20}!'.format(nome)) #Prazer em te conhecer      Guilherme      !
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Prazer em te conhecer =====Guilherme======!
