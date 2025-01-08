# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar 
# que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('-=-'*20)
print('                  Análisador de triangúlos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
    if r1 == r2 == r3: # Condição aninhada
        print('É um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo ESCALENO')
    else:
        print('É um triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

