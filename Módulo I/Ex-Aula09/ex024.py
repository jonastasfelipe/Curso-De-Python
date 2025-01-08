#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome da sua cidade: ').strip()
a = cidade.split()
b = (a[0].upper())
print('Começa com o nome "Santo"?', ('SANTO'in b))

#Resolução do exercício
#cid = str(input('Em que cidade você nasceu? ')).strip()
#print(cid[:5].upper() == 'SANTO')

#Os dois funcionam 