'''Curso Python #013 - Estrutura de repetição 'for'

Laço de repetição
Laço com variável de controle
laço = for
Em português
laço c no intervalo(1,10) # o 'c' é a variavel de contrele
    passo
pega
'''
'''
for c in range(1,10):
    passo
pega
'''
'''Em português
laço c no intervalo(0,3)
    passo
    pula    
passo
pega'''

'''
for c in range(0,3):
    passo
    pula
passo
pega
'''
'''Em português
laço c no intervalo(0,3)
    se moeda
        pega
    passo
    pula    
passo
pega'''

'''
for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega
'''

#PRÁTICA
for c in range(0,6): #Repete 'Oi' 6 vezes
    print('Oi')
print('FIM')
###############################
for c in range(0,6): #Conta de 0 a 5
    print(c)
print('FIM')
##############################
for c in range(6,0,-1): #Conta de 5 a 0
    print(c)
print('FIM')
#################################
for c in range(0,7,2): #Conta de 0 a 6 pulando de 2 em 2 
    print(c)
print('FIM')
#################################
n = int(input('Digite um número: ')) #Faz uma contagem de 0 ao número digitado
for c in range(0, n+1):
    print(c)
print('FIM')
#################################
i = int(input('Início: ')) #Conta a partir do 'Início' até o 'Fim' a cada 'Passo'
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM')
###################################
for c in range(0,3): #Vai pedir para digitar o valor 3 vezes
    n = int(input('Digite um valor:'))
print('FIM')
#####################################
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
