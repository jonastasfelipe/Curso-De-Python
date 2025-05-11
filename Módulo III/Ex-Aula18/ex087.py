# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  
somapar = 0
somaimpar = 0
soma_coluna = 0
maior = 0
for i in range(0, 3): 
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]:  '))  
        if matriz[i][j] % 2 == 0:  # Verifica se o valor é par
            somapar += matriz[i][j] # Soma os valores pares
        if matriz[i][j] % 2 != 0:  # Verifica se o valor é ímpar 
            somaimpar += matriz[i][j]      
print('-=' * 15)
for i in range(0, 3): 
    for j in range(0, 3): 
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print() 
print('-=' * 15)
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores ímpares é: {somaimpar}')
for i in range(0, 3): 
    soma_coluna += matriz[i][0]  # Soma os valores da primeira coluna
print(f'A soma dos valores da primeira coluna é: {soma_coluna}')
for i in range(0, 3): 
    soma_coluna += matriz[i][1]  # Soma os valores da segunda coluna
print(f'A soma dos valores da segunda coluna é: {soma_coluna}')
for i in range(0, 3):
    soma_coluna += matriz[i][2]  # Soma os valores da terceira coluna
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
for j in range(0, 3): 
    if matriz[0][j] > maior:  # Verifica o maior valor da primeira linha
        maior = matriz[0][j]
print(f'O maior valor da primeira linha é: {maior}')
 