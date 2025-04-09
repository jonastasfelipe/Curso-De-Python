#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
valor = 0
for i in range(7): #Lê 7 valores
    valor = int(input(f'Digite o {i+1}° valor: ')) 
    if valor % 2 == 0: #Verifica se o valor é par ou ímpar
        num[0].append(valor) 
    else:
        num[1].append(valor) 
print('-='*30)
print(f'A lista completa é: {num}') 
print(f'A lista de pares é: {sorted(num[0])}') 
print(f'A lista de ímpares é: {sorted(num[1])}') 
print('-='*30)
