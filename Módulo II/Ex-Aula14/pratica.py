'''for c in range (1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''for c in range (1, 5):
   n = int(input('Digite um valor: '))
print('Fim')
'''
# Neste código o programa só para quando o valor digitado for 0
'''n = 1
while n != 0: # flag = condição de parada
   n = int(input('Digite um valor: '))
print('Fim')'''
'''
r ='' 'S'
while r == 'S':
   n = int(input('Digite um valor: '))
   r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''
n = 1 
par = impar = 0
while n != 0:
   n = int(input('Digiete um valor: '))
   if n != 0:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
