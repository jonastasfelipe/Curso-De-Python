# Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado 
# for negativo. 
while True:
    n = int(input('QUER VER A TABUADA DE QUAL VALOR?: ')) 
    if n < 0:
        break
    print(40*'-')
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print(40*'-')
print('PROGRAMA TABUADA ENCERRADO')
    