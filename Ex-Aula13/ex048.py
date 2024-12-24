'''Faça um programa que calcule a soma entre 
todos os números que são múltiplos de três e que se encontram no 
intervalo de 1 até 500.'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # toda vez que for encontrado um valor que seja divisível por 3 em 'cont += 1' vai contar a quantidade de valores, qunado for 'soma += c' vai somar todos os valores 
        cont += 1 # cont = cont + 1
        soma += c # soma = soma + c
        print(c, end=' ')
print('''
A soma de todos os {} valores solicitados é {}'''.format(cont, soma))