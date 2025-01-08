# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar 
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos 
cont_idade = 0
cont_m = 0
cont_f = 0
while True: 
    print(30*'-')
    print('CADASTRE UMA PESSOA')
    print(30*'-')
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1
    cadastro = ' '
    while cadastro not in 'SN':
        cadastro = input('Gostaria de contrinuar o cadastro? [S/N]: ').strip().upper()[0]
    if cadastro == 'N':
        break
print(30*'-')
print(f'Tem {cont_idade} pessoas com mais de 18 anos cadastradas.')
print(f'Tem {cont_m} homens cadastrados.')
print(f'Tem {cont_f} mulheres com menos de 20 anos cadastradas')
print(30*'-')