#O mesmo professor do desaio anterior quer sortear a ordem de apresentação de 
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
# e mostre a ordem sorteada

from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]
shuffle(lista) # Em uma sequência (embaralha os itens da lista)
print('A ordem de apresentação será')
print(lista)
