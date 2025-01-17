#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores.count(valores[-1]) > 1: #Se o último valor digitado for duplicado
        print('Valor duplicado! Não vou adicionar...')
        valores.pop()
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'S':
        continue
    elif r == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')