#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Criação da matriz 3x3 com valores iniciais 0
for i in range(0, 3):  # Loop para percorrer as linhas da matriz
    for j in range(0, 3): # Loop para percorrer as colunas da matriz
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]:  '))  # Leitura do valor para cada posição da matriz
print('-=' * 15)
for i in range(0, 3): 
    for j in range(0, 3): 
        print(f'[{matriz[i][j]:^5}]', end=' ') # Impressão da matriz formatada, centralizando os valores em um espaço de 5 caracteres
    print() # Pula para a próxima linha após imprimir uma linha da matriz