# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
# mostre os 10 primeiros termos dessa progressão.
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo = int(input('Primeiro termo: ')) # onde eu quero que comece
razao = int(input('Razão: ')) # de quanto eu quero que some ex;"2 em 2 ou 3 em 3" 
decimo = termo + (10 - 1) * razao # fórmula para saber o décimo termo e pode ser alterado mudando o primeiro número que está entre parenteses "(*10*-1)"
for c in range(termo, decimo + razao, razao): 
    print('{}'.format(c), end =' → ')
print('ACABOU')
