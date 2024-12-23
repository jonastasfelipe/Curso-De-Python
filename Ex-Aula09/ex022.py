#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quatas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome=(input('Digite o seu nome completo: '))
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
junto=''.join(nome.split())
print('Seu nome ao todo tem {} letras'.format(len(junto)))
primeiro=nome.split()
primeiro=primeiro[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro,len(primeiro)))
