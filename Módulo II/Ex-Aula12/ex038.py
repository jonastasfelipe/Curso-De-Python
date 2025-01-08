# Escreva um programa que leia dois números inteiros e 
# compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O numero {} é maior que o número {}'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior que o número {}'.format(num2, num1))
elif num1 == num2:
    print('O valor {} é igual ao valor {}'.format(num1, num2))

# Resolução do exercício
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO número é maior')
else:
    print('Os dois valores são iguais')
    