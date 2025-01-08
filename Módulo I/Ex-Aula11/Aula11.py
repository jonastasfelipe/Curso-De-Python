''' ANSI ==> escape sequence'''

# \033[ ==> Começo do código | m ==> Final do código
# No meio do código fica ==> style = 0; | text = 33; | back = 44;
# Exemplo montado ==> \033[0;33;44m
# Os principais códigos para style são: 0 = none  1 == bold  4 = underline  7 = negative
# Os principais códigos para text(Cor da letra) são: 30 = white 31 = red 32 = green 33 = yellow 34 = blue 35 = purple 36 = cyan 37 = gray
# Os principais códigos para back(Cor do fundo) são: 40 = white 41 = red 42 = green 43 = yellow 44 = blue 45 = purple 46 = cyan 47 = gray

#Testes
print('\033[1;30;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[1;35;43mTESTE\033[m')
print('\033[1;30;42mTESTE\033[m')
print('\033[mTESTE\033[m')
print('\033[7;30mTESTE\033[m')

# Teste 2
a = 3
b = 5
print('Os valores são \033[1;31m{}\033[m e \033[1;33m{}\033[m!!!'.format(a, b))

# Teste 3
nome = 'Jonatas'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Teste 4
nome = 'Jonatas'
cores = {'limpa':'\033[m', 
         'azul':'\033[34m',
         'amarelo': '\033[33m', 
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

