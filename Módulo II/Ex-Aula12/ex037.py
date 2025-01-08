# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

'''número = int(input('Digíte um número: '))
conversão = int(input('Digite 1 para binário, 2 para octal e 3 para hexadeximal e 0 para conversão geral:'))
if conversão == 1:
    print('O número {} convertido para bínário é {}'.format(número, bin(número)))
elif conversão == 2:
    print('O número {} convertido para octal é {}'.format(número, oct(número)))
elif conversão == 3:
    print('O número {} convertido para hexadecimal é {}'.format(número, hex(número)))
elif conversão == 0:
    print('O número {} convertido para binário: {},'.format(número, bin(número)), end='')
    print(' octal: {},'.format(oct(número)), end='')
    print(' hexadeximal: {}'.format(hex(número)))
else:
    print('ERRO: Confira se você selecionou os números para conversão corretamente "1,2,3"')
'''
# Resolução do exercício
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # Esse '[2:]' é uma técnica de fatiamento, significa que só vai contar a partir da terceira posição porque quando é convertido as duas primeiras posições são de identificação ex;'0b, 0o, 0x' 
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
