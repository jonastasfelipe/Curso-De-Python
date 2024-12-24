# Faça um programa que leia o ano de nascimento de um jovem e 
# informe, de acordo com a sua idade, se ele ainda vai se 
# alistar ao serviço militar, se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. Seu programa também 
# deverá mostrar o tempo que falta ou que passou do prazo.

'''ano = int(input('Digite o ano do seu nascimento: '))
passa = 2006 - ano
falta = ano - 2006
if ano > 2006:
    print('Você ainda vai se alistar no serviço militar')
    print('Falta {} anos para se alistar'.format(falta))
elif ano == 2006:
    print('É a hora certa para se alistar')
else:
    print('Já passou do tempo de se alistar')
    print('Está {} anos atrasado'.format(passa))
'''

# Resolução do exercício
from datetime import date
atual = date.today().year # Data da máquina
print('''Qual o seu gênero? 
[ 1 ] Masculino
[ 2 ] Feminino''') # Extra
opção = int(input('Sua opção: ')) # Extra
if opção == 2:
    print('Você não precisa fazer o alistamento militar obrigátorio') # Extra
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda Faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))



