#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite o último número: '))
tupla = (num, num1, num2, num3)
print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição' if 3 in tupla else 'O valor 3 não foi digitado')
for n in tupla:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram: {n}', end=' ')