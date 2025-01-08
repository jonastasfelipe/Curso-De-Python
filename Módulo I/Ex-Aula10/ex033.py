# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c    
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
