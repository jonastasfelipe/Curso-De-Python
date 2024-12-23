#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez 
#Em que posição ela aparece a última vez

#frase=input('Digite uma frase: ')
#print('A letra "a" aprece {} vezes'.format(frase.count('a')))
#print('Na posição {}'.format(frase.find('a')))
#print('A ultima {}'.format(frase.rfind('a')))

#Resolução do exercício 
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))