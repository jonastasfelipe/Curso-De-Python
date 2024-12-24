# Faça um programa que leia um ano qualquer e mostr3e se ele é BISSEXTO

'''
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 ano % 100 != 0 or ano % 400 == 0: # O ano tem que ser divisível por 4 e também não pode ser divisivel por 100 ou então o ano ser divisível por 400
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
'''

# Pegando o ano do computador
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # função para reconhecer o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # O ano tem que ser divisível por 4 e também não pode ser divisivel por 100 ou então o ano ser divisível por 400
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano)) 